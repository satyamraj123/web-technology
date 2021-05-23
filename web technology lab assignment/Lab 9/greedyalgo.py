n = int(input())
coins = 0
while(n > 0):
    if(n >= 10):
        n -= 10
        coins += 1
    elif(n >= 5):
        n -= 5
        coins += 1
    else:
        coins += n
        n = 0
print(coins)
