n=5
a=[]
for i in range(0,n):
    integer=int(input("Enter any integer:"))
    a.append(integer)
sum1=0
sum2=0
sum3=0
for j in a:
    if j>0:
        sum1=sum1+j
    else:
        sum2=sum2+j
print("Sum of all positive integers is",sum1)
print("Sum of all negative integers is",sum2)
sum3=sum1+sum2
avg=sum3/n
print("Average of all integers is",avg)
print("Number above average is")
for k in range(len(a)):
    if a[k]>avg:
        print(a[k],end=" ")