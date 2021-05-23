n, m = map(int, input().split())
list1 = [0, 1, 1]
for i in range(3, n+1):
    list1.append(list1[i-1]+list1[i-2])
    if(i != 3 and (list1[i] % m == 1 and list1[i-1] % m == 1 and list1[i-2] % m == 0)):
        break
lengthofperiod = len(list1)-3
if(n < len(list1)):
    print(list1[n] % m)
else:
    print(list1[n % lengthofperiod] % m)
