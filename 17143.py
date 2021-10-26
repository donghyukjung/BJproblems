
#######################################
# [BJ_17143] 낚시왕
# https://www.acmicpc.net/problem/17143
# ....일단 해보장
#######################################


# (r,c) : coord (start w/ 1),
# s : speed
# d: direction(1-up 2-down 3-right 4-left)
# z : size
def printM(M):
    n, m = len(M), len(M[0])
    print("------------------------------------------\nprint matrix\n")
    for i in range(n):
        for j in range(m):
            print("%3d" % M[i][j], end=" ")
        print()
    print("\nprint matrix end\n------------------------------------------")
    
R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]
fisher = 0
for i in range(M):
    sharks[i][2] %= 2*R-2 if sharks[i][3] >= 3 else 2*C-2

printM(sharks)
sharks.sort(key=lambda x:(x[0], x[1]))
printM(sharks)
#######################################
# Let shark's state is x0 and width n.
# s%=s/(2*n)
# in right way, 
# if 0 <= s <= n - x0, x = x0+s
# if n - x0 < s <= 2n - x0, x = 2n - x0 - s
# if 2n - x0 < s < 2n, x = s + x0 - 2n
#
# in reverse,
# if s <= x0, x = x0 - s
# if s <= n + x0, x = s - x0
# if s <= 2n, x = 2n + x0 - s
#######################################
dir[_, []]
answer = 0
for fisher in range(R):

    # get shark
    idx, max = -1, 101
    for i in range(M):
        if sharks[i][0] == fisher and sharks[i][1] < max:
            idx, max = i, sharks[i][1]
    if idx > -1:
        answer += sharks[idx][4]
        del sharks[idx]
        M -= 1

    # shark move
    for i in range(M):
        r, c, s, d, z = sharks[i]
        if d >= 3:  # len : R
            n, x0 = R-1, r
            if d == 3:
                if s <= n-x0:
                    r = x0+s
                elif s <= 2*n-x0:
                    r = 2*n - x0 - s
                    d = 4
                else:
                    r = s + x0 - 2*n
            else:
                if s <= x0:
                    r = x0-s
                elif s < n+x0:
                    r = s-x0
                    d = 3
                else:
                    r = 2*n + x0 - s
        else:  # len : C
            n, x0 = C-1, c
            if d == 3:
                if s <= n-x0:
                    c = x0+s
                elif s <= 2*n-x0:
                    c = 2*n - x0 - s
                    d = 4
                else:
                    c = s + x0 - 2*n
            else:
                if s <= x0:
                    c = x0-s
                elif s < n+x0:
                    c = s-x0
                    d = 3
                else:
                    c = 2*n + x0 - s

    sharks[i] = r, c, s, d, z
    sharks.sort(key=lambda x:(x[0], x[1]))

    # shark predation
# shark predation
