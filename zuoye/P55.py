s = input("输入")
if len(s) > 20:
    print(s[:20])
else:
    n = "{:=^20}".format(s)
    print(n)
