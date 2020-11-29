# Abhishek Anand
# Mean and Median
n=int(input())
a=list(map(int,input().split()))
mean=sum(a)/n
if n%2!=0:
    median=a[n//2]
else:
    median=(a[n//2-1]+a[n//2])/2

print(mean,median)

