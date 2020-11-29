# Abhishek Anand
# Binary Search
def BinarySearch(arr,n,k):
    i=0
    j=n-1
    
    while i<=j:
        mid=(i+j)//2
        if a[mid]==k:
            return mid+1
        elif a[mid]>k:
            j=mid-1
        else:
            i=mid+1
    return -1
        
    
n=int(input())
a=list(map(int,input().split()))
k=int(input())
print(BinarySearch(a,n,k))
