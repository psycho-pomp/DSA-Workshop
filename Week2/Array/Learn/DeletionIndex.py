# Abhishek Anand
# Deletion if index is given
        
    
n=int(input())
a=list(map(int,input().split()))
k=int(input())
del a[k]
a.pop(k)
print(a)

