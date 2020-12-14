def print_matrix(m,r,c):
    for i in range(r):
        for j in range(c):
            print(m[i][j],end=" ")
        print()
def subtract_matrix(matrix1,matrix2,res_matrix,r,c):
    for i in range(r):
        for j in range(c):
            res_matrix[i][j]=matrix1[i][j]-matrix2[i][j]
    
r1,c1=map(int,input().split())
matrix1=[]
for i in range(r1):
    matrix1.append(list(map(int,input().split())))
r2,c2=map(int,input().split())
matrix2=[]
for i in range(r2):
    matrix2.append(list(map(int,input().split())))
if r1==r2 and c1==c2:
    res_matrix=matrix1[:][:]
    subtract_matrix(matrix1,matrix2,res_matrix,r1,c1)
    print_matrix(res_matrix,r1,c1)
else:
    print("Cannot Subtract")
