def leastdiff(arr,length,n):
    mindiff=arr[0]-n
    mindiffele=arr[0]
    for i in range(1,length):
        diff=arr[i]-n
        if diff<mindiff:
            mindiff=diff
            mindiffele=arr[i]
    return mindiffele
length=int(input())
arr=int(input().strip())
n=int(input())
print(leastdiff(arr,length,n))