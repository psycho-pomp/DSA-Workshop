
def print_matrix(m,r,c):
    for i in range(r):
        for j in range(c):
            print(m[i][j],end=" ")
        print()
def matrix_rotation(a,r,c):
    n=r
    for i in range(n//2):
        for j in range(i,n-1-i):
            temp=a[i][j]
            a[i][j]=a[j][n-1-i]
            a[j][n-1-i]=a[n-1-i][n-1-j]
            a[n-1-i][n-1-j]=a[n-1-j][i]
            a[n-1-j][i]=temp
            
            
    
m,n=map(int,input().split())
a=[]
for i in range(m):
    a.append(list(map(int,input().split())))
matrix_rotation(a,m,n)
print_matrix(a,m,n)

