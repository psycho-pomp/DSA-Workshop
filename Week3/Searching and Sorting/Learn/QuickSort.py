# Abhishek Anand
# Quick Sort--Taking last element as piviot
def partition(arr,low,high):
    i=low-1
    piviot=arr[high]
    for j in range(low,high):
        if arr[j]<piviot:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
            
    
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
    
        

def QuickSort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        QuickSort(arr,low,pi-1)
        QuickSort(arr,pi+1,high)

    
n=int(input())
a=list(map(int,input().split()))
QuickSort(a,0,n-1)
print(a)
        
        
