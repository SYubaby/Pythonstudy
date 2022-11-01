'''
对不同的对象设置不同的初始化属性
传参数
'''

#1 _定义类 带参数的init, 宽度和高度， 实例方法： 电泳实例属性


class Washer():

    #定义_init_,添加实例属性

    def __init__(self, width, height):
        self.width = width
        self.length = height

    def print_info(self):  # self 指的是调用该函数的对象
        #类里面获取实例属性
        print(f'洗衣机的宽度{self.width}, 洗衣机的宽度{self.length}')

s
#2. 创建对象，创建多个对象且属性值不同：调用实例方法
haier1 = Washer(10, 20)
haier1.print_info()

haier2 = Washer(30, 40)
haier2.print_info()




