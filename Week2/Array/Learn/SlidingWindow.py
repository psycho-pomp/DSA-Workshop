# Abhishek Anand
# Sliding Window
def SlidingWindow(arr,n,k):
    if k>n:
        return
    s=sum(arr[:k])
    max_sum=s
    for i in range(n-k):
        s=s-arr[i]+arr[i+k]
        max_sum=max(s,max_sum)
    return max_sum
        
        
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
print(SlidingWindow(arr,n,k))
