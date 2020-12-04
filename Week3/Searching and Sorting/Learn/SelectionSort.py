
# Abhishek Anand
# Selection Sort
def SelectionSort(arr,n):
    
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[min_idx],arr[i]=arr[i],arr[min_idx]
    
        
    
    
        

n=int(input())
a=list(map(int,input().split()))
SelectionSort(a,n)
print(a)
        
        
