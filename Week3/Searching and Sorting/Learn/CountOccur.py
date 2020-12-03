# Abhishek Anand
# Count number of Occurences in Sorted Array
def first_occur(arr,start,end,k):
    res=-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]>k:
            end=mid-1
        elif arr[mid]<k:
            start=mid+1
        else:
            res=mid
            end=mid-1
    return res
def last_occur(arr,start,end,k):
    res=-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]>k:
            end=mid-1
            
        elif arr[mid]<k:
            start=mid+1
        else:
            res=mid
            start=mid+1
            
    return res

n=int(input())
a=list(map(int,input().split()))
k=int(input())
print(last_occur(a,0,n-1,k)-first_occur(a,0,n-1,k)+1)
        
        
