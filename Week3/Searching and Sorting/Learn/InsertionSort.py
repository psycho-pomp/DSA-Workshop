# Abhishek Anand
# Insertion Sort
def InsertionSort(arr,n):
    
    for i in range(1,n):
        key=a[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    
    
        

n=int(input())
a=list(map(int,input().split()))
InsertionSort(a,n)
print(a)
        
        
