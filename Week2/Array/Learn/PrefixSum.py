# Abhishek Anand
# Prefix_Sum
def Prefix_Sum(arr,n):
    
    prefix_sum[0]=arr[0]
    for i in range(1,n):
        prefix_sum[i]=arr[i]+prefix_sum[i-1]
    #print(prefix_sum)
    return max(prefix_sum)
        
        
n=int(input())
arr=list(map(int,input().split()))
prefix_sum=[0]*n
print(Prefix_Sum(arr,n))
print(*prefix_sum)
