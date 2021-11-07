
#######################################
# BJ_07576 : 토마토
# https://www.acmicpc.net/problem/7576
# 정말 멍청하게 틀렸다
#######################################

from collections import deque
import sys

input = sys.stdin.readline
N, M, L = map(int, input().split())
map = [[list(map(int, input().split())) for i in range(M)] for _ in range(L)]
visited = [[[0 for i in range(N)] for j in range(M)] for k in range(L)]
q = deque()

# Find 1 and add to queue
for i in range(L):
    for j in range(M):
        for k in range(N):
            if map[i][j][k] == 1:
                visited[i][j][k] = 1
                q.append([i, j, k])

# run bfs
dir = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]

while q:
    x, y, z = q.popleft()
    for dx, dy, dz in dir:
        nx, ny, nz = x+dx, y+dy, z+dz
        if 0 <= nx < L and 0 <= ny < M and 0 <= nz < N and map[nx][ny][nz] == 0 and (visited[nx][ny][nz] > visited[x][y][z]+1 or visited[nx][ny][nz] == 0):
            q.append([nx, ny, nz])
            visited[nx][ny][nz] = visited[x][y][z]+1

# check result
max = 0
sw = 0
for i in range(L):
    for j in range(M):
        for k in range(N):
            if max < visited[i][j][k]:
                max = visited[i][j][k]
            if visited[i][j][k] == 0 and map[i][j][k] == 0:
                sw = 1

if sw == 1:
    print(-1)  # not changed completely
elif max == 0:
    print(0)  # no tomatos to change
else:
    print(max-1)  # print day
