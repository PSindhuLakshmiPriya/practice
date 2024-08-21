def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i*i<=num:
        if num%i==0 or num%(i+2)==0:
            return False
        i +=6
    return True
n, *numbers = map(int,input().split())
q=min(numbers)
p=q
while p<10**10:
    remainder_check=all((p%x==q)for x in numbers if x!=q)
    if remainder_check and is_prime(p):
        print(p)
        break
    p += 1
else:
    print("None")
    