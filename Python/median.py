import statistics
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr1.sort()
arr2.sort()
result=statistics.median(arr1,arr2)
print(result)