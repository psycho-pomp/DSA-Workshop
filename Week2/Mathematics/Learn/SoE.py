# Abhishek Anand
# Sieve of Eratosthenes
n=int(input())
p=[True]*(n+1)
p[0]=False
p[1]=False
x=2
while x*x<=n:
    if p[x]:
        for i in range(x*2,n+1,x):
            p[i]=False
    x+=1
for i in range(n):
    if p[i]:
        print(i)
