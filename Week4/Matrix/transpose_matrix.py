
def print_matrix(m,r,c):
    for i in range(r):
        for j in range(c):
            print(m[i][j],end=" ")
        print()
def transpose_matrix(a,m,n,c):
    for i in range(n):
        for j in range(m):
            c[i][j]=a[j][i]
            
            
    
m,n=map(int,input().split())
a=[]
for i in range(m):
    a.append(list(map(int,input().split())))
c=[]
for i in range(n):
    c.append([0]*m)

transpose_matrix(a,m,n,c)
print_matrix(c,n,m)

