from math import sqrt

x0, y0, x1, y1 = list(map(float, filter(lambda it: it != "", input().split(" "))))
print(sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2))
