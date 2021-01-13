Wt=list(map(int,input().split()))
V=list(map(int,input().split()))
W=int(input())
t=[[-1 for i in range(W+1)] for j in range(n+1)]

def knapsack(Wt,V,W,n):
    if W==0 or n==0:
        return 0
    
    if t[n][W]!=-1:
        return t[n][W]
    
    if Wt[n-1]<=W:
        t[n][W]=max(V[n-1]+knapsack(Wt,V,W-Wt[n-1],n-1),knapsack(Wt,V,W,n-1))
        return t[n][W]
    else:
        t[n][W]=knapsack(Wt,V,W,n-1)
        return t[n][W]
print(knapsack(Wt,V,W,n))

        
