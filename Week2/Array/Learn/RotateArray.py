# Abhishek Anand
# Array Rotation-Without Extra Space--O(N*K)
def rotateArray(arr,n,d):
    d%=n
    for i in range(d):
        temp=a[0]
        for j in range(n-1):
            a[j]=a[j+1]
        a[n-1]=temp
            
        
    return arr
#pythonic way:----res=arr[d:]+res[0:d]    
    
n=int(input())
a=list(map(int,input().split()))
d=int(input())
print(rotateArray(a,n,d))
