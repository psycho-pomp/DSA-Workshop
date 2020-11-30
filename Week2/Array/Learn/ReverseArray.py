# Abhishek Anand
# Reversing Array-Without Extra Space
def ReverseArray(arr,start,end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
        
n=int(input())
arr=list(map(int,input().split()))
ReverseArray(arr,0,n-1)
print(arr)
