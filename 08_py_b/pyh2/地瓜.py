class potato:
    how=''
    tk=''
    T=0
    def __init__(self,T,tk):
        self.T=T
        self.tk=tk
        if T<10:
            self.how='生的'
        else:
            self.how='熟的'
    def __str__(self):
        return self.tk
    def add(self):
        self.how+=self.tk
        print(self.how)
time=int(input('请输入烤土豆时间'))
tk=input('请输入加的调料')
n=potato(T=time,tk=tk)
n.add()
