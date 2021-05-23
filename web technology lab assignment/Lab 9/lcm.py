a, b = map(int, input().split())

if(a > b):
    i = a
else:
    i = b

while(True):
    if(i % a == 0 and i % b == 0):
        print(i)
        break
    if(a > b):
        i = i+a
    else:
        i = i+b
