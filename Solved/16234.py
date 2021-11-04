
def printM(M):
    n, m = len(M), len(M[0])
    print("print matrix")
    for i in range(n):
        for j in range(m):
            print("%4d" % M[i][j], end=" ")
        print()


import math as m
from collections import deque

N, L, R = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
dir = [[1,0],[0,1],[-1,0],[0,-1]]


def BFS1(i, j, idx):
    q = deque()
    q.append((i, j))
    visited[i][j] = idx
    temp = []
    flag = 1
    while q:
        x, y = q.popleft()
        temp.append((x, y, P[x][y]))
        for dx,dy in dir:
            if x+dx >= N or x+dx < 0 or y+dy >= N or y+dy < 0:
                continue
            diff = m.fabs(P[x][y]-P[x+dx][y+dy])
            if diff>=L and diff<=R and visited[x+dx][y+dy] == 0:
                visited[x+dx][y+dy], flag = idx, 0
                q.append((x+dx, y+dy))

    num, sum = len(temp), 0
    if num == 1:
        return flag
    for n in range(num):
        sum += temp[n][2]
    avg = sum//num
    for n in range(num):
        x, y, _ = temp[n]
        P[x][y] = avg
    return flag


cnt = 0
while True:
    idx, flag = 1, 1
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # Open the border
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                flag *= BFS1(i, j, idx)
                idx += 1
    if flag:
        break
    else:
        cnt += 1

print(cnt)
