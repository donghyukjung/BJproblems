#######################################
# BJ_14502 : 연구소                     
# https://www.acmicpc.net/problem/14502
# BFS와 Brute-Force를 활용
# optimize : 적절한 케이스에 따라 pruning
#######################################

def printM(M):
    n, m = len(M), len(M[0])
    print("------------------------------------------\nprint matrix\n")
    for i in range(n):
        for j in range(m):
            print("%3d" % M[i][j], end=" ")
        print()
    print("\nprint matrix end\n------------------------------------------")


from collections import deque
from itertools import combinations

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def BFS(x0,y0):
    q=deque()
    q.append((x0,y0))
    visited[x0][y0]=1
    while q:
        x,y=q.popleft()
        visited[x][y]=1
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if map[nx][ny] != 1 and visited[nx][ny] == 0:
                # visited[nx][ny] = 1
                q.append((nx, ny))

candidate = [(i, j) for i in range(N) for j in range(M) if map[i][j] == 0]
virus = [(i, j) for i in range(N) for j in range(M) if map[i][j] == 2]
can_num=len(candidate)
v_num = len(virus)
C=list(combinations(candidate,3))
n=len(C)
print("# of combination: ",n)

max=0
for i in range(n):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for x,y in C[i]:
        map[x][y]=1
    # Virus spread
    for x,y in virus:
        BFS(x,y)       
    
    cnt=0
    valid=True
    for x in range(N):
        for y in range(M):
            cnt+= 1 if (map[x][y] != 1 and visited[x][y] == 0) else 0
    max=cnt if cnt>max else max
    for x,y in C[i]:
        map[x][y]=0
print(max)