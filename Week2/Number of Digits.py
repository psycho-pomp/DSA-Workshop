# Abhishek Anand
# Counting no of digits-Iterative Approach
n=int(input())
count=0
while n!=0:
    count+=1
    n//=10
print(count)
