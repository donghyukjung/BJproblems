#######################################
# BJ_07576 : 토마토
# https://www.acmicpc.net/problem/7576
# 정말 멍청하게 틀렸다
#######################################

from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
map = [list(map(int, input().split())) for i in range(M)]
visited = [[0 for i in range(N)] for j in range(M)]
q = deque()

# Find 1 and add to queue
for i in range(M): 
    for j in range(N):
        if map[i][j] == 1:
            visited[i][j] = 1
            q.append([i, j])

# run bfs
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

while q:
    x, y = q.popleft()
    for dx, dy in dir:
        nx, ny = x+dx, y+dy
        if 0 <= nx < M and 0 <= ny < N and map[nx][ny] == 0 and (visited[nx][ny] > visited[x][y]+1 or visited[nx][ny]==0):
            q.append([nx, ny])
            visited[nx][ny] = visited[x][y]+1
            
# check result
max = 0
sw = 0
for i in range(M):
    for j in range(N):
        if max < visited[i][j]:
            max = visited[i][j]
        if visited[i][j] == 0 and map[i][j] == 0:
            sw = 1

if sw == 1:
    print(-1)  # not changed completely
elif max == 0:
    print(0)  # no tomatos to change
else :
    print(max-1) # print day
