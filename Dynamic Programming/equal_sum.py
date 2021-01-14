
        

n=int(input())
arr=list(map(int,input().split()))
    
def equal_sum(arr,n):
    if sum(arr)%2!=0:
        return False
    else:
        req_sum=sum(arr)//2
        t=[[False for j in range(req_sum+1)] for i in range(n+1)]
        for i in range(n+1):
            t[i][0]=True
        
        for i in range(1,n+1):
            for j in range(1,req_sum+1):
                if arr[i-1]<=j:
                    t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
        return t[n][req_sum]

print(equal_sum(arr,n))

        
