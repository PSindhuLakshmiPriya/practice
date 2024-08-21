import math
n=int(input())
rem=n%10
if rem<=4:
    print(((n//10)*10))
else:
    print(((n//10)+1)*10)