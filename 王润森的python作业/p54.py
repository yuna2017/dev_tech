import math

# 输入坐标
x0, y0, x1, y1 = map(int, input("请输入两个坐标,每两个数字间有一个空格").split())

# 计算距离
d = (math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2))

# 输出
print(d)
