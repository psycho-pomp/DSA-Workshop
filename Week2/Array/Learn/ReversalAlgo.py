# Abhishek Anand
# Array Rotation-Reversal Algorithim
def reverseArray(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
def rotateArray(arr,n,d):
    d%=n
    reverseArray(arr,0,d-1)
    reverseArray(arr,d,n-1)
    reverseArray(arr,0,n-1)
    return arr
    
n=int(input())
a=list(map(int,input().split()))
d=int(input())
print(rotateArray(a,n,d))
