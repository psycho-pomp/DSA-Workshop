# Abhishek Anand
# Missing and Repeating Number-Make two equations using Sum and Product 
import math
def MissRep(arr,n):
    arr_sum=sum(arr)
    arr_mul=1
    for i in range(n):
        arr_mul*=a[i]
    org_sum=(n*(n+1))//2
    org_mul=(math.factorial(n))
    y=((org_sum-arr_sum)*(arr_mul))//(org_mul-arr_mul)
    x=(y*(org_mul))//(arr_mul)
    return [x,y]
n=int(input())
a=list(map(int,input().split()))
print(MissRep(a,n))
        
        
