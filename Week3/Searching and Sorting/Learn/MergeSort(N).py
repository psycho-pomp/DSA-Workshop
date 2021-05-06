# Abhishek Anand
# Merge Sort
def MergeSort(arr,l,r):
    if l<r:
        mid=(l+r)//2
        MergeSort(arr,l,mid)
        MergeSort(arr,mid+1,r)
        Merge(arr,l,r,mid)
def Merge(arr,l,r,m):
    
    n1=m-l+1
    n2=r-m
    L=[0]*n1
    R=[0]*n2
    for i in range(n1):
        L[i]=arr[(l+i)]
    for j in range(n2):
        R[j]=arr[(m+1+j)]
        
    i=0
    j=0
    k=l
    while i<n1 and j<n2:
        if L[i]<R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        arr[k]=R[j]
        k+=1
        j+=1
n=int(input())
a=list(map(int,input().split()))
MergeSort(a,0,n-1)
print(*a)
    

