# Abhishek Anand
# Quick Sort--Taking random element as piviot
import random
def QuickSort(arr,low,high):
    if low<high:
        pi=partitionrand(arr,low,high)
        QuickSort(arr,low,pi-1)
        QuickSort(arr,pi+1,high)
def partitionrand(arr,low,high):
    rand_piviot=random.randrange(low,high)
    arr[low],arr[rand_piviot]=arr[rand_piviot],arr[low]
    return partition(arr,low,high)
def partition(arr,low,high):
    i=low+1
    piviot=arr[low]
    for j in range(low+1,high+1):
        if arr[j]<=piviot:
            arr[j],arr[i]=arr[i],arr[j]
            i+=1
    arr[i-1],arr[low]=arr[low],arr[i-1]
    return i-1
n=int(input())
a=list(map(int,input().split()))
QuickSort(a,0,n-1)
print(a)
