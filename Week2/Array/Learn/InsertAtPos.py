# Abhishek Anand
# Insertion in array at a position
n=int(input())
a=list(map(int,input().split()))
k,ele=map(int,input().split())
a.insert(k,ele)
print(a)
