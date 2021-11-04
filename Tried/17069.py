#######################################
# BJ_17069 : 파이프 옮기기 2 (1과 같은문제 : 17070)
# https://www.acmicpc.net/problem/17069
# DP로 풀면되는데.... 경계조건에서 걸리는 듯 하다
#######################################

N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

zeros = [0, 0, 0]
arr = [[zeros for col in range(N)] for row in range(N)]

# initialize
arr[0][1] = [0, 0, 1]

for c in range(0, N):
    for r in range(1, N):
        if c == 0:
            if r == 0 or r == 1:
                continue

        t1, t2, t3 = 1-M[c-1][r], 1-M[c-1][r-1], 1 - M[c][r-1]
        arr[c][r] = [(arr[c-1][r][0]+arr[c-1][r][1]*t2)*t1*t3,
                     (arr[c-1][r-1][0]+arr[c-1][r-1][1]+arr[c-1][r-1][2])*t1*t2*t3,
                     (arr[c][r-1][1]*t2+arr[c][r-1][2])*t1*t3]

# for c in range(0,N) :
#     for r in range(0,N) :
#         print("(",c,",",r,":",M[c][r],")",arr[c][r], end=" : ")
#     print()

print(arr[N-1][N-1][0]+arr[N-1][N-1][1]+arr[N-1][N-1][2])
