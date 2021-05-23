n = int(input())
list1 = list(map(int, input().split()))
max1 = 0
max2 = 0
maxindex = 0
for i in range(0, n):
    if(max1 < list1[i]):
        max2 = max1
        max1 = list1[i]
        maxindex = i
    if(i != maxindex and max2 < list1[i]):
        max2 = list1[i]
print(max1*max2)
