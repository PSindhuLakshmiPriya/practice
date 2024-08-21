def findCount(length,arr,num,diff):
    count=0
    for i in range(length):
        if abs(arr[i]-num)<=diff:
            count+=1
    return count
length=int(input())
arr=list(map(int,input().split()))
num=int(input())
diff=int(input())
print(findCount(length,arr,num,diff))