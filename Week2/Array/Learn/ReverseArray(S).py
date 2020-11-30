# Abhishek Anand
# Reversing Array-With Extra Space
def ReverseArray(arr,start,end):
    if start>=end:
        return
    temp=[]
    for i in range(end,start-1,-1):
        temp.append(arr[i])
    for j in range(start,end+1):
        arr[i]=temp[i]
        
n=int(input())
arr=list(map(int,input().split()))
ReverseArray(arr,0,n-1)
print(arr)
