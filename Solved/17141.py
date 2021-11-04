#######################################
# BJ_17141 : 연구소 2                    
# https://www.acmicpc.net/problem/17141
# BFS와 Brute-Force를 활용
# optimize : 적절한 케이스에 따라 pruning
# 바이러스 후보 중 선택 ->
#######################################

def printM(M):
    n, m = len(M), len(M[0])
    print("------------------------------------------\nprint matrix\n")
    for i in range(n):
        for j in range(m):
            if M[i][j]<0:
                print(" #",end=" ")
            else:
                print("%2d" % M[i][j], end=" ")
        print()
    print("\nprint matrix end\n------------------------------------------")

from collections import deque
from itertools import combinations

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1 for _ in range(N)] for _ in range(N)]
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def BFS(x0,y0):
    q=deque()
    q.append((x0,y0))
    visited[x0][y0]=0
    while q:
        x,y=q.popleft()
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if map[nx][ny] != 1 and (visited[nx][ny] == -1  or visited[nx][ny]>visited[x][y]+1):
                visited[nx][ny] = visited[x][y] +1
                q.append((nx, ny))


candidate = [(i, j) for i in range(N) for j in range(N) if map[i][j] == 2]
num=len(candidate)
C=list(combinations(candidate,M))
n=len(C)
max=50*50
for i in range(n):
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    for x,y in C[i]:
        map[x][y]=2 if (x,y) in C else 0
    # Virus spread
    for x,y in C[i]:
        BFS(x,y)       
    
    time=0
    valid=True
    for x in range(N):
        for y in range(N):
            if visited[x][y]>time:
                time=visited[x][y]
            if visited[x][y]==-1 and map[x][y]==0:
                valid=False

    if time<max and valid:
        max=time

    for x,y in C[i]:
        map[x][y]=2

if max==50*50 and not valid:
    max=-1
print(max)