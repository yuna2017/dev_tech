class SweetPotato:
    def __init__(self, time, status, seasoning):
        self.time = time
        self.status = status
        self.seasoning = seasoning

    def roast(self, roast_time):
        self.time += roast_time
        if self.time < 3:
            self.status = '生的'
        elif self.time < 5:
            self.status = '半生不熟'
        elif self.time < 8:
            self.status = '熟的'
        else:
            self.status = '烤糊了'

    def add_seasoning(self, seasoning):
        self.seasoning += seasoning

    def __str__(self):
        return f'烤地瓜状态：{self.status}，被烤时间：{self.time}分钟，添加的调料：{self.seasoning}'
