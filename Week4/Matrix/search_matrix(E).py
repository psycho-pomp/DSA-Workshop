
def print_matrix(m,r,c):
    for i in range(r):
        for j in range(c):
            print(m[i][j],end=" ")
        print()
def search_matrix(a,n,x):
    i,j=0,n-1
    while i<n and j>=0:
        if a[i][j]==x:
            print("Found at ",i,j)
            return True
        elif a[i][j]>x:
            j-=1
        else:
            i+=1
    return False
            
            
    
m,n=map(int,input().split())
a=[]
for i in range(m):
    a.append(list(map(int,input().split())))
x=int(input())

search_matrix(a,n,x)
#print_matrix(,n,m)


        
    
