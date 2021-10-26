########################################################
# GG 비활성이 활성을 만나면, 그때부터 활성이 되는거임
# 그래서 뭔가 잘못생각한듯 하다
# 단순히 패스라고 생각한게 오인이였다
# 활성화는 시간이 아님!
# 연구로 1번부터 차레로 풀기
########################################################

#######################################
# BJ_17142 : 연구소 3                    
# https://www.acmicpc.net/problem/17142
# BFS와 Brute-Force를 활용
# optimize : 적절한 케이스에 따라 pruning
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
                if map[nx][ny]==-2: 
                    # if deactivated virus
                    visited[nx][ny] = visited[x][y]    
                else :
                    # if blank
                    visited[nx][ny] = visited[x][y] +1
                q.append((nx, ny))

candidate = [(i, j) for i in range(N) for j in range(N) if map[i][j] == 2]
num=len(candidate)
C=list(combinations(range(num),M))
n=len(C)
print("# of combination: ",n)

max=50*50
for i in range(n):
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    for j in range(num):
        x,y=candidate[j]
        map[x][y]=2 if j in C[i] else -2
    # Virus spread
    for j in C[i]:
        x,y=candidate[j]
        BFS(x,y)       
    
    time=0
    valid=True
    for x in range(N):
        for y in range(N):
            if visited[x][y]>time:
                time=visited[x][y]
            if visited[x][y]==-1 and map[x][y]==0:
                valid=False
    printM(visited)
    
    if time<max and valid:
        max=time

    for j in range(num):
        x,y=candidate[j]
        map[x][y]=2
if max==50*50 and not valid:
    max=-1
print(max)


# In optimize step, 
# def BFS(x0, y0, idx):
#     q = deque()
#     q.append((x0, y0))
#     while q:
#         x, y = q.popleft()
#         visited[x][y] = idx
#         for dx, dy in dir:
#             nx, ny = x+dx, y+dy
#             if nx >= N or nx < 0 or ny >= N or ny < 0:
#                 continue
#             if map[nx][ny] != 1 and visited[nx][ny] == 0:
#                 visited[nx][ny] == idx
#                 q.append((nx, ny))
#     return True
# region = 1
# for i in range(N):
#     for j in range(N):
#         if map[i][j] != 1 and visited[i][j] == 0:
#             BFS(i, j, region)
#             region += 1

# for i in range(M):
#     x, y, _ = candidate[i]
#     candidate[i][2] == visited[x][y]
