'''
烤地瓜

需求
'''
# 1. 定义类：初始化属性， 被烤 和 添加调料的方法，显示对象信息的str

class SweetPotato():

    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 地瓜的状态
        self.cook_state = '生的'
        # 调料列表
        self.condiments = []  # 很多种所以列表

#1 被烤的时间和  对应的地瓜状态 0-3mins 生的  3-5 半生不熟
# 判断地瓜被烤的总时间是在哪个区间，修改地瓜的状态
    def cook(self, time): # time参数接收看时间
        #烤地瓜的方法：
        #1：先计算地瓜整体烤过的时间
        self.cook_time += time
        #2. 用整体烤过的时间再判断地瓜的状态
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_state = 'Done'
        elif self.cook_time >= 8:
            self.cook_state = '烤糊了'

# 添加的调料：用户根据自己的意愿添加
    def add_condiments(self, condiment):
        #添加调料
        self.condiments.append(condiment)


# 2.显示对象信息
    def __str__(self):
        return f'这个地瓜烤了{self.cook_time}, 状态是{self.cook_state}, 添加的调料有{self.condiments}'

 # 3. 创建对象并调用对应的实例方法
digua1 = SweetPotato()

print(digua1)

digua1.cook(2)
digua1.add_condiments('辣椒面')
print(digua1)

digua1.cook(2)
digua1.add_condiments('黑胡椒')
print(digua1)

digua1.cook(2)
digua1.add_condiments('白砂糖')
print(digua1)

