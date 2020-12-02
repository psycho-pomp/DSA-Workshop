# Abhishek Anand
# Ternary Search
def TernarySearch(arr,l,r,k):
    
    while r>=l:
        
        mid1=l+((r-l)//3)
        mid2=r-((r-l)//3)
        if arr[mid1]==k:
            return mid1
        if arr[mid2]==k:
            return mid2
        
        if k<arr[mid1]:
            r=mid1-1
        elif k>arr[mid2]:
            l=mid2+1
        else:
            l=mid1+1
            r=mid2-1
    return -1
n=int(input())
a=list(map(int,input().split()))
k=int(input())
print(TernarySearch(a,0,n-1,k))
        
