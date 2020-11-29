# Abhishek Anand
# trailing zero's in factorial
n=int(input())
count=0
p=5
while p<=n:
    count+=(n//p)
    p*=5
print(count)

    
