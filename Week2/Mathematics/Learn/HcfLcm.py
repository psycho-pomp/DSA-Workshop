# Abhishek Anand
# GCD & LCM
a,b=map(int,input().split())
mul=a*b
while b:
    a,b=b,a%b
gcd=a
lcm=(mul//gcd)
print(gcd,lcm)
            
