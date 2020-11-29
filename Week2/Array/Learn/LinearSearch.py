# Abhishek Anand
# Linear Search
def LinearSearch(arr,k):
    for i in range(n):
        if arr[i]==k:
            return i+1
    return -1
n=int(input())
a=list(map(int,input().split()))
k=int(input())
res=LinearSearch(a,k)
print(res)
