len1=int(input())
arr1=list(map(int,input().split()))
len2=int(input())
arr2=list(map(int,input().split()))
k=int(input())
a=0
b=0
for i in range(len1):
    if(arr1[i]>k):
        a=a+1
for j in range(len2):
    if(arr2[j]<k):
        b=b+1
print(max(a,b))
