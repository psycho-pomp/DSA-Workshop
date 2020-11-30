# Abhishek Anand
# Reversing Array-Without Extra Space
def ReverseArray(arr,start,end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    start+=1
    end-=1
    ReverseArray(arr,start,end)
        
n=int(input())
arr=list(map(int,input().split()))
ReverseArray(arr,0,n-1)
print(arr)
