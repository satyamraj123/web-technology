list1 = [4, 2, 5, 1]
list2 = [2, 4, 4, 4]
count = 0
for i in list1:
    for j in list2:
        if i == j:
            count = count+1
            break
print(count)
