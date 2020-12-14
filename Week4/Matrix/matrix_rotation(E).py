#Abhishek Anand
def print_matrix(m,r,c):
    for i in range(r):
        for j in range(c):
            print(m[i][j],end=" ")
        print()
def matrix_rotation(a,r,c):
    temp=[]
    for i in range(r):
        x=[]
        for j in range(c):
            x.append(a[i][j])
        temp.append(x)
    
    for i in range(r):
        for j in range(c):
            a[i][j]=temp[j][c-1-i]
            
    
m,n=map(int,input().split())
a=[]
for i in range(m):
    a.append(list(map(int,input().split())))
matrix_rotation(a,m,n)
print_matrix(a,m,n)
