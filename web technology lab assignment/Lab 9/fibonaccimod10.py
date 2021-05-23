# same code as fibonacc1
# put m=10 here
n = int(input())
list1 = [0, 1, 1]
for i in range(3, n+1):
    list1.append(list1[i-1]+list1[i-2])
    if(i != 3 and (list1[i] % 10 == 1 and list1[i-1] % 10 == 1 and list1[i-2] % 10 == 0)):
        break
lengthofperiod = len(list1)-3
if(n < len(list1)):
    print(list1[n] % 10)
else:
    print(list1[n % lengthofperiod] % 10)
