# Abhishek Anand
# Missing and Repeating Number-sorting and traversing
def MissRep(arr,n):
    arr.sort()
    Repeating=0
    Missing=1
    for i in range(1,n):
        if arr[i]-arr[i-1]==0:
            Repeating=arr[i-1]
        if arr[i]-arr[i-1]==2:
            Missing=arr[i]-1
    return [Missing,Repeating]
n=int(input())
a=list(map(int,input().split()))
print(MissRep(a,n))
        
        
