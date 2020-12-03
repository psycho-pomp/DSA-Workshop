# Abhishek Anand
# Count number of Occurences in Sorted Array
def find_peak(arr,start,end,n):
    mid=(start+end)//2
    if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid+1]<=arr[mid]):
        return mid
    elif arr[mid-1]>arr[mid]:
        return find_peak(arr,start,mid-1,n)
    else:
        return find_peak(arr,mid+1,end,n)
    return -1
        

n=int(input())
a=list(map(int,input().split()))

print(find_peak(a,0,n-1,n))
        
