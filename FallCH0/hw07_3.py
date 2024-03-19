class Roast_Potato:
    time=0
    status="0"
    seasoning=[]
    def judgestatus(self):
        if self.time>0 and self.time<=3:
            self.status="生的"
        elif self.time>3 and self.time<=5:
            self.status="半生不熟"
        elif self.time>5 and self.time<=8:
            self.status="熟的"
        elif self.time>8:
            self.status="烤糊了"
    def __init__(self,time):
        self.time=time
        self.judgestatus()
    def changetime(self):
        print("输入时间：")
        Time=input()
        self.time=Time
        print("更改成功！")
    def addseasoning(self):
        print("输入添加的调料：")
        season=input()
        self.seasoning.append(season)
        print("添加成功！")
    def __str__(self):
        return str(f"烤地瓜时间：{self.time} 地瓜状态：{self.status} 添加的调料：{self.seasoning}")
testpotato=Roast_Potato(2)
print(testpotato)
testpotato.changetime()
testpotato.addseasoning()
print(testpotato)
