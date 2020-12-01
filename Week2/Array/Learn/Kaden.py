# Abhishek Anand
# Maximum Contigiuos sum--Kaden's Algorithm
def MaxSubArrSum(arr,n):
    curr_max=arr[0]
    max_so_far=arr[0]
    for i in range(1,n):
        curr_max=max(arr[i],curr_max+arr[i])
        max_so_far=max(curr_max,max_so_far)
    return max_so_far
    

n=int(input())
arr=list(map(int,input().split(",")))
print(MaxSubArrSum(arr,n))
