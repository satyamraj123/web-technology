n = int(input())
list1 = [0, 1, 1]
for i in range(3, n+1):
    list1.append(list1[i-1]+list1[i-2])
    if(i != 3 and (list1[i] % 10 == 1 and list1[i-1] % 10 == 1 and list1[i-2] % 10 == 0)):
        break


if(n <= 60):
    lengthofperiod = len(list1)-1
else:
    lengthofperiod = len(list1)-3


list2 = [0, 1, 2]
for i in range(3, lengthofperiod+1):
    list2.append(list2[i-1]+list1[i])

if(n < len(list2)):
    print(list2[n] % 10)
else:
    print(list2[n % lengthofperiod] % 10)
