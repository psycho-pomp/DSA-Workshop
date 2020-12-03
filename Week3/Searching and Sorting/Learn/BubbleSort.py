# Abhishek Anand
# Insertion Sort
def BubbleSort(arr,n):
    
    for i in range(n):
        swapped=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if swapped==False:
            break
        
    
    
        

n=int(input())
a=list(map(int,input().split()))
BubbleSort(a,n)
print(a)
        
        
