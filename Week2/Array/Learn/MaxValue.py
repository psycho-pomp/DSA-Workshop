# Abhishek Anand
# Maximum value in an array after m range increment operations
def Prefix_Sum(arr,n):
    prefix_sum=[0]*n
    prefix_sum[0]=arr[0]
    for i in range(1,n):
        prefix_sum[i]=arr[i]+prefix_sum[i-1]
    return (prefix_sum)
def Max_Sum(arr,n,m):
    for i in range(m):
        a,b,k=map(int,input().split())
        arr[a]+=k
        arr[b+1]-=k
    return max(Prefix_Sum(arr,n))
    
    
    
    
        
        
n=int(input())
#arr=list(map(int,input().split()))
arr=[0]*n
m=int(input())
print(Max_Sum(arr,n,m))
