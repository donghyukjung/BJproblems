N = int(input())

arr=[0 for i in range(N)]
arr[0]=1
cnt=2
for i in range(2,N+1):
    # print("i=",i, ", cnt=",cnt)
    sw=0
    for j in range(1,N):
        # print("    j=",j)
        if i*j>N: break
        if arr[j*i-1]==0:
            arr[j*i-1]=cnt
            sw=1
            # print("arr[",i*j,"] is changed into ",cnt)
    if sw==1 : 
        cnt+=1
    

print(cnt-1)
for e in arr : print(e,end=" ")