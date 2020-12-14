def search_matrix(m,r,c,k):
    for i in range(r):
        for j in range(c):
            if m[i][j]==k:
                return True
    return False
    
r,c=map(int,input().split())
matrix=[]
for i in range(r):
    matrix.append(list(map(int,input().split())))
key=int(input())
print(search_matrix(matrix,r,c,key))
        
    
