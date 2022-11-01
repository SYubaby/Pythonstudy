'''
_xx_()的函数
具有特殊功能的函数

1. 定义类

    init 魔法方法： width 和height
    添加实例方法：访问实例属性

2. 创建对象
3. 验证成果
调用实例方法

__init__ 在创建对象是默认被调用，不需要手动调用
self 参数不需要开发者传递，自动把当前对象引用传递过去
'''

#_init_() 方法的作用：初始化对象

class Washer():

    #定义_init_,添加实例属性

    def __init__(self):
        self.width = 400
        self.length = 500

    def print_info(self):  # self 指的是调用该函数的对象
        #类里面获取实例属性
        print(f'haier1的宽度{self.width}')
        print(f'haier1的宽度{self.length}')

haier1 = Washer()


haier1.print_info()





