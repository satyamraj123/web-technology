# cook your dish here
from numpy.random import randint


def positionofpointwrtline(x, y, x1, y1, x2, y2):
    ans = 0
    ans = y-y1-(y2-y1)/(x2-x1)*(x-x1)
    if(ans > 0):
        return False
    elif(ans == 0):
        return True
    else:
        return True


def mod(x):
    if(x >= 0):
        return x
    else:
        return 0-x


def fastalgo(list1, n):
    i = 0
    maxdistance = 0
    j = i+1
    maxheightlineinbetween = []
    while(j < n):
        if(j > i):
            if(maxheightlineinbetween == []):
                maxheightlineinbetween = [j, list1[j]]
                if(maxdistance < mod(i-j)):
                    maxdistance = mod(i-j)
            elif(positionofpointwrtline(maxheightlineinbetween[0], maxheightlineinbetween[1], i, list1[i], j, list1[j]) == True):

                maxheightlineinbetween = [j, list1[j]]
                if(maxdistance < mod(i-j)):
                    maxdistance = mod(i-j)
            else:
                if(maxheightlineinbetween[1] >= list1[i] and positionofpointwrtline(maxheightlineinbetween[0], maxheightlineinbetween[1], i, list1[i], j, list1[j]) == False and n-maxheightlineinbetween[0]-1 > maxdistance):
                    i = maxheightlineinbetween[0]
                    maxheightlineinbetween = []
                    j = i+1
                    continue
        j = j+1

    i = n-1
    j = n-2
    maxheightlineinbetween = []
    while(j >= 0):
        if(j < i):
            if(maxheightlineinbetween == []):
                maxheightlineinbetween = [j, list1[j]]
                if(maxdistance < mod(i-j)):
                    maxdistance = mod(i-j)
            elif(positionofpointwrtline(maxheightlineinbetween[0], maxheightlineinbetween[1], i, list1[i], j, list1[j])):
                maxheightlineinbetween = [j, list1[j]]
                if(maxdistance < mod(i-j)):
                    maxdistance = mod(i-j)
            else:
                if(maxheightlineinbetween[1] >= list1[i] and positionofpointwrtline(maxheightlineinbetween[0], maxheightlineinbetween[1], i, list1[i], j, list1[j]) == False and n-maxheightlineinbetween[0]-1 <= maxdistance):
                    i = maxheightlineinbetween[0]
                    maxheightlineinbetween = []
                    j = i-1
                    continue
        j = j-1

    return maxdistance


def correctalgo(list1, n):
    i = 0
    maxdistance = 0
    while(i < n):
        j = i+1
        maxheightlineinbetween = []
        while(j < n):
            if(j > i):
                if(maxheightlineinbetween == []):
                    maxheightlineinbetween = [j, list1[j]]
                    if(maxdistance < mod(i-j)):
                        maxdistance = mod(i-j)
                elif(positionofpointwrtline(maxheightlineinbetween[0], maxheightlineinbetween[1], i, list1[i], j, list1[j])):
                    maxheightlineinbetween = [j, list1[j]]
                    if(maxdistance < mod(i-j)):
                        maxdistance = mod(i-j)
            else:
                break
            j = j+1
        i = i+1
    return maxdistance


while(True):

    n = randint(0, 6)
    inputlist = randint(1, 10, n)
    #n = 5
    #inputlist = [5, 9, 4, 6, 5]
    x = fastalgo(inputlist, n)
    y = correctalgo(inputlist, n)

    if(x != y):
        print("Failed at")
        print(n)
        print(inputlist)
        print("Fast algo answer="+str(x))
        print("Correct algo answer="+str(y))
        break
