def print_matrix(m,r,c):
    for i in range(r):
        for j in range(c):
            print(m[i][j],end=" ")
        print()
r,c=map(int,input().split())
matrix=[]
for i in range(r):
    matrix.append(list(map(int,input().split())))
print_matrix(matrix,r,c)
        
    
