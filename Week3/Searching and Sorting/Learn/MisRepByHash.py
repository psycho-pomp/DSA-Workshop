# Abhishek Anand
# Missing and Repeating --Hash
import math
def MissRep(arr,n):
    d={}
    Missing=0
    Repeating=0
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in range(1,n+1):
        
        if i not in d:
            Missing=i
        else:
            if d[i]==2:
                Repeating=i
    return [Missing,Repeating]
            
n=int(input())
a=list(map(int,input().split()))
print(MissRep(a,n))
