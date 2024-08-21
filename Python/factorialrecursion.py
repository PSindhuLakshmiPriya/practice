def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
num=7
if num<0:
    print("not exist foe negative integers")
elif num==0:
    print("factorial is 1")
else:
    print("factorial is",factorial(num))