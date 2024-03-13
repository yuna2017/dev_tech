s=input()
if len(s)<=20:
    print("{:=^20}".format(s))
else:
    print(s[0:20])