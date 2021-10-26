import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
map = [list(map(int, input().split())) for i in range(M)]

q = deque()
# Find 1
for i, j in enumerate(map):  # i : index, j : list
    if 1 in j:
        q.append([i, j.index(1)])

# run bfs
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < M and 0 <= ny < N and map[nx][ny] == 0:
            q.append([nx, ny])
            map[nx][ny] = map[x][y]+1

# check result 
max=1
sw=0
for i in range(M):
    for j in range(N):
        if max<map[i][j] : max=map[i][j]
        if map[i][j]==0 : sw=1

if max==1 : print(0) # no tomatos to change
elif sw==1 : print(-1) # not changed completely
else : print(max-1) # print day
