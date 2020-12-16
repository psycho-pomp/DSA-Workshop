

def print_matrix(m,r,c):
    for i in range(r):
        for j in range(c):
            print(m[i][j],end=" ")
        print()
def spiralprint_matrix(a,m,n):
    k=0
    l=0
    while k<m and l<n:
        for i in range(l,m):
            print(a[k][i],end=" ")
        k+=1
        
        for i in range(k,n):
            print(a[i][n-1],end=" ")
        n-=1
        
        if k<m:
            for i in range(n-1,l-1,-1):
                print(a[m-1][i],end=" ")
            m-=1
        if l<n:
            for i in range(m-1,k-1,-1):
                print(a[i][l],end=" ")
            l+=1
    
            
            
    
m,n=map(int,input().split())
a=[]
for i in range(m):
    a.append(list(map(int,input().split())))


spiralprint_matrix(a,m,n)
#print_matrix(,n,m)


        
    
