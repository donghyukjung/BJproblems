from collections import deque

def dfs(v):
    print(v,end=" ")
    visit_dfs[v]=1
    for i in range(1,N+1):
        if visit_dfs[i]==0 and G[v][i]==1:
            dfs(i)

def bfs(v):
    q=deque()
    q.append(v)
    visit_bfs[v]=1
    while q:
        v=q.popleft()
        print(v,end=" ")
        for i in range(1,N+1):
            if visit_bfs[i]==0 and G[v][i]==1:
                q.append(i)
                visit_bfs[i]=1

N,M,V = map(int, input().split())

G=[[0]*(N+1) for _ in range(N+1)]
visit_dfs=[0]*(N+1)
visit_bfs=[0]*(N+1)

for _ in range(M):
    v1, v2 = map(int, input().split())
    G[v1][v2]=1
    G[v2][v1]=1

dfs(V)
print()
bfs(V)