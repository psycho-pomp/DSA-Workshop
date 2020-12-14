def print_matrix(m,r,c):
    for i in range(r):
        for j in range(c):
            print(m[i][j],end=" ")
        print()
def multiply_matrix(a,b,c,m,n,p,q):
    for i in range(m):
        for j in range(q):
            for k in range(n):
                c[i][j]+=a[i][k]*b[k][j]
    
m,n=map(int,input().split())
a=[]
for i in range(m):
    a.append(list(map(int,input().split())))
p,q=map(int,input().split())
b=[]
for i in range(p):
    b.append(list(map(int,input().split())))
if n==p:
    c=[]
    for i in range(m):
        c.append([0]*q)
        
    multiply_matrix(a,b,c,m,n,p,q)
    print_matrix(c,m,q)
else:
    print("cannot perform operation")

        
    
