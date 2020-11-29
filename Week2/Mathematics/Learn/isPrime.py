#User function Template for python3
from math import sqrt,ceil
def isPrime(N):
    # code here
    if N>1:
        for i in range(2,ceil(sqrt(N))+1):
            if N%i==0:
                return False
        return True
    else:
        return False
