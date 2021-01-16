n=int(input())
arr=list(map(int,input().split()))
req_sum=int(input())
t=[[0 for j in range(req_sum+1)] for i in range(n+1)]
for i in range(n+1):
    t[i][0]=1
    
def count_subset_sum(arr,req_sum,n):
    
    for i in range(1,n+1):
        for j in range(1,req_sum+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    return t[n][req_sum]


print(count_subset_sum(arr,req_sum,n))
