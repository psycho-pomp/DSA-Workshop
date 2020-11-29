# Abhishek Anand
# Array Rotation-Extra Space
def rotateArray(arr,n,d):
    d%=n
    temp=[]
    for i in range(d):
        temp.append(arr[i])
    for i in range(n-d):
        arr[i]=arr[i+d]
    j=0
    for i in range(n-d,n):
        arr[i]=temp[j]
        j+=1
    return arr
#pythonic way:----res=arr[d:]+res[0:d]    
    
n=int(input())
a=list(map(int,input().split()))
d=int(input())
print(rotateArray(a,n,d))
