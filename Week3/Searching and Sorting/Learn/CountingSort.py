# Abhishek Anand
# Counting Sort
def CountingSort(arr):
    min_ele=min(arr)
    max_ele=max(arr)
    range_of_elements=max_ele-min_ele+1
    size=len(arr)
    count=[0 for i in range(range_of_elements)]
    output=[0 for i in range(size)]
    for i in range(size):
        count[arr[i]-min_ele]+=1
    for i in range(1,range_of_elements):
        count[i]+=count[i-1]
        
    for i in range(size-1,-1,-1):
        output[count[arr[i]-min_ele]-1]=arr[i]
        count[arr[i]-min_ele]-=1
    for i in range(size):
        arr[i]=output[i]
    
n=int(input())
a=list(map(int,input().split()))
CountingSort(a)
print(*a)
    
