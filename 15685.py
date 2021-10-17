N = int(input())  # 1~20
curves = [list(map(int, input().split())) for _ in range(N)]  # x,y,d,g

max_gen = 0
# Find maximum generation
for i in range(N): max_gen = curves[i][3] if curves[i][3] > max_gen else max_gen

M = 101
map = [[0 for col in range(M)] for row in range(M)]
dir = [[1, 0], [0, -1], [-1, 0], [0, 1]]
d_arr = [0, 1]

# Calculate curve directions
for i in range(1, max_gen):
    len = 2**i
    for j in range(len): d_arr.append((d_arr[j]+2) % 4 if j < len/2 else d_arr[j])

# Draw Curve
for i in range(N):
    x, y, d, g = curves[i]
    px, py = x, y
    map[px][py] = 1
    len = 2**g
    for i in range(len):
        px, py = px+dir[(d_arr[i]+d) % 4][0], py+dir[(d_arr[i]+d) % 4][1]
        map[px][py] = 1

# Check answer
cnt = 0
for i in range(M-1):
    for j in range(M-1):
        if map[i][j] & map[i+1][j] & map[i][j+1] & map[i+1][j+1]: cnt += 1
print(cnt)
