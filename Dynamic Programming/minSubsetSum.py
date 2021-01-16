n=int(input())
arr=list(map(int,input().split()))
req_sum=sum(arr)
t=[[False for j in range(req_sum+1)] for i in range(n+1)]
for i in range(n+1):
    t[i][0]=True
    
def subset_sum(arr,req_sum,n):
    
    for i in range(1,n+1):
        for j in range(1,req_sum+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
subset_sum(arr,req_sum,n)
mn=req_sum
for j in range(req_sum//2+1):
    if t[n][j]==True:
        mn=min(req_sum-2*j,mn)

print(mn)
