input_str = input("输入四个用空格分隔的数字")
x0,y0,x1,y1= map(float,input_str.split())
s = ((x1-x0)**2 + (y1-y0)**2)**0.5
print("两点的距离为:",s)
