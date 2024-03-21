class Washer:
    def __init__(self):
        self.wash_time = 0
        self.wash_cleanliness = '脏的'
        self.ingredients = []

    def wash(self, time):
        self.wash_time += time
        if 0 <= self.wash_time < 5:
            self.wash_cleanliness = '不干不净，穿衣没事'
        elif 5 <= self.wash_time < 10:
            self.wash_cleanliness = '衣服洗的不错哦'
        elif 10 <= self.wash_time < 20:
            self.wash_cleanliness = '洗一件衣服用不了20分钟吧？！'
        elif 20 <= self.wash_time < 30:
            self.wash_cleanliness = '一件衣服洗20多分钟，孩子你生活技能是0？'

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def __str__(self):
        return f'这件衣服洗了{self.wash_time}分钟，状态是{self.wash_cleanliness}，添加的成分为{self.ingredients}'

clothes = Washer()
print(clothes)

clothes.wash(2)
clothes.add_ingredient('立白洗衣液')
print(clothes)

clothes.wash(6)
clothes.add_ingredient("蓝月亮洗衣液")
print(clothes)
