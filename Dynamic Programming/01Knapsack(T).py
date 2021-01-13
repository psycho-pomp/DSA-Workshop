n=int(input())
Wt=list(map(int,input().split()))
V=list(map(int,input().split()))
W=int(input())
t=[[0 for j in range(W+1)] for i in range(n+1)]

def knapsack(Wt,V,W,n):
    #t=[[0 for j in range(W+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
            if Wt[i-1]<=j:
                t[i][j]=max(V[i-1]+t[i-1][j-Wt[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    return t[n][W]

print(knapsack(Wt,V,W,n))

        
