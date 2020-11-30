# Abhishek Anand
# Range Sum
def Prefix_Sum(arr,n):
    
    prefix_sum[0]=arr[0]
    for i in range(1,n):
        prefix_sum[i]=arr[i]+prefix_sum[i-1]
    return (prefix_sum)
def Range_Sum(arr,i,j):
    pre=Prefix_Sum(arr,n)
    if i==0:
        return pre[j]
    else:
        return pre[j]-pre[i-1]
    
    
        
        
n=int(input())
arr=list(map(int,input().split()))
i,j=map(int,input().split())
prefix_sum=[0]*n
print(Range_Sum(arr,i,j))
