import math
x0, y0, x1, y1 = map(float, input().split())
distance = math.sqrt((x1-x0)**2+(y1-y0)**2)
print("两点之间的距离为:",distance)
