pointt1 = list(map(int, input().split()))
pointt2 = list(map(int, input().split()))
pointt3 = list(map(int, input().split()))

# point 1 and point2 will make the striaght line, and we will find whether point3 lies above or below the line
# y-y1=(y2-y1)/(x2-x1)*(x-x1)
# y-y1-(y2-y1)/(x2-x1)*(x-x1)
y = pointt3[1]
x = pointt3[0]
y1 = pointt1[1]
x1 = pointt1[0]
y2 = pointt2[1]
x2 = pointt2[0]
ans = 0
ans = (y-y1)-((y2-y1)/(x2-x1))*(x-x1)
print(ans)
if(ans > 0):
    print("point3 lies above line through point1, point2")
elif(ans == 0):
    print("point3 instersects the line through point1, point2")
else:
    print("point3 lies below line through point1, point2")
