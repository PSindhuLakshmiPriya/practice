n=int(input())
temp=n
sum=0
while temp>1:
    rem=temp%10
    sum=sum+(rem*rem)
    temp=temp//10
if temp==1:
    print(n,"is a happy number")
else:
    print(n,"is not a happy number")
