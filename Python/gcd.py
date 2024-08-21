n1=int(input())
n2=int(input())
gcd=1
n3=min(n1,n2)
for i in range(1,n3):
    if n1%i==0 and n2%i==0:
        gcd=i
print("GCD of two numbers is",gcd)