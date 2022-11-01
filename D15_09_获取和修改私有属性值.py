'''
get_xx用来获取私有属性，定义set_xx 用来修改私有属性值 不是必须get or set
'''
#经典类：class 类名新式类： class 类名（object）

# 默认继承object类， object 是顶级类 或基类，其他子类叫派生类

#1. 师父类
class Master(object):
    def __init__(self):
        # name
        self.kongfu = '[初始配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


#创建学校类
class School(object):
    def __init__(self):
        # name
        self.kongfu = '[学校的配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


#2 徒弟类
#子类B：添加和父类同名的属性和方法
class Prentic(School, Master):
    def __init__(self):
        # name
        self.kongfu = '[自己的配方]'
        #定义私有属性
        self.__money = 200000000

    #定义函数：获取私有属性值 get_xx

    def get_money(self):
        return self.__money
    #定义修改函数
    def set_money(self):
        self.__money = 500


        #定义私有方法
    def __info_print(self):
        print('私有方法')

    def make_cake(self):
        self.__init__()  # 原因： 不加这个自己的初始化，kongfu属性值是上一次调用的init 内的kongfu 属性值
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)  # 不初始化调用不了self 。 想要调用父类的同名和属性， 属性在init初始化位置
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


class Tusun(Prentic):
    pass



Peter2 = Tusun()
print(Peter2.get_money())

Peter2.set_money()

print(Peter2.get_money())