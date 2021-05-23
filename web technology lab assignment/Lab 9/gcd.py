def gcdfun(a, b):
    if(b == 0):
        return a
    r = a % b
    return gcdfun(b, r)


n, m = map(int, input().split())
print(gcdfun(n, m))
