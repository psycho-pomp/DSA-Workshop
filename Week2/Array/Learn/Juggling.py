# Abhishek Anand
# Array Rotation Juggling Algorithm
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def rotateArray(arr,n,d):
    d%=n
    g=gcd(d,n)
    for i in range(g):
        temp=arr[i]
        j=i
        while(1):
            k=j+d
            if k>=n:
                k-=n
            if k==i:
                break
            arr[j]=arr[k]
            j=k
        arr[j]=temp
    return arr
    
n=int(input())
a=list(map(int,input().split()))
d=int(input())
print(rotateArray(a,n,d))
