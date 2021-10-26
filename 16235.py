
#######################################
# [BJ_16235] 나무 재테크
# https://www.acmicpc.net/problem/16235
# 자료구조 설계가 중요할듯?
#######################################

def printM(M):
    n, m = len(M), len(M[0])
    print("------------------------------------------\nprint matrix\n")
    for i in range(n):
        for j in range(m):
            print(M[i][j], end=" ")
        print()
    print("\nprint matrix end\n------------------------------------------")

N, M, K = map(int, input().split())
nutrients=[list(map(int, input().split())) for _ in range(N)]
tree=[(list(map(int, input().split()))) for _ in range(M)]

#land : consist of nutrients and numbers
land=[[[5, []]for i in range(N)]for j in range(N)]
for x,y,age in tree:
    land[x-1][y-1][1].append(age)
for x,y,_ in tree:
    land[x-1][y-1][1].sort()
    
dir=[[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]

def spring():
    for x in range(N):
        for y in range(N):
            nu, arr = land[x][y]
            for i in range(len(arr)):
                flag=True if nu>=arr[i] else False
                if flag:    
                    nu-=arr[i]
                    arr[i]+=1
                else : 
                    arr[i]*=-1
            land[x][y]=[nu,arr]
    return

def summer():
    for x in range(N):
        for y in range(N):
            nu, arr = land[x][y]
            for i in range(len(arr)):
                if arr[i]<0:  
                    nu+=((-arr[i])//2)                         
            land[x][y]=[nu,arr]      
    return

def autumn():
    for x in range(N):
        for y in range(N):
            nu, arr = land[x][y]
            for i in range(len(arr)):
                if arr[i]>0 and arr[i]%5==0:
                    for dx, dy in dir:
                        nx, ny = x+dx, y+dy
                        if nx >= N or nx < 0 or ny >= N or ny < 0:
                            continue
                        land[nx][ny][1].insert(0,1)
    return

def winter():
    for i in range(N):
        for j in range(N):
            land[i][j][0]+=nutrients[i][j]
    return 

for i in range(K):
    spring()
    summer()
    autumn()
    winter()
    # print("spring")
    # printM(land)
    # print("summer")
    # printM(land)
    # print("autumn")
    # printM(land)
    # print("winter)")
    # printM(land)

num=0
for x in range(N):
    for y in range(N):
        _ , arr = land[x][y]
        for e in arr:
            if e>0: num+=1
        
print(num)