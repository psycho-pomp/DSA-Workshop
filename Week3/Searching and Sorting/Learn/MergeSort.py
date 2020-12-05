# Abhishek Anand
# Merge Sort--Pythonic
def MergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        MergeSort(l)
        MergeSort(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            arr[k]=r[j]
            k+=1
            j+=1
n=int(input())
a=list(map(int,input().split()))
MergeSort(a)
print(*a)
