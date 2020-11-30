# Abhishek Anand
# Reversing Array-Without Extra Space
def ReverseArray(arr,start,end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
        
n=int(input())
arr=list(map(int,input().split()))
ReverseArray(arr,0,n-1)
print(arr)
