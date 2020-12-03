# Abhishek Anand
# Missing and Repeating --Negative index
import math
def MissRep(arr,n):
    for i in  range(n):
        if arr[abs(arr[i])-1]<0:
            Repeating=abs(arr[i])
        else:
            arr[abs(arr[i])-1]=-arr[abs(arr[i])-1]
    #print(arr)
    for i in range(n):
        if arr[i]>0:
            Missing=i+1
    return [Missing,Repeating]
            
n=int(input())
a=list(map(int,input().split()))
print(MissRep(a,n))
        
        
