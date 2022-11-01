'''
子类调用父类的同名方法和属性
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

#如果先调用了父类的属性和方法，父类属性会覆盖子类属性，故在调用属性前，先调用自己子类的初始化
    def make_cake(self):
        self.__init__()  # 原因： 不加这个自己的初始化，kongfu属性值是上一次调用的init 内的kongfu 属性值
        print(f'运用{self.kongfu}制作煎饼果子')

#调用父类方法，但是为保证调用到的也是父类的属性，必须在条用方法前调用父类的初始化
    def make_master_cake(self):
        Master.__init__(self)  # 不初始化调用不了self 。 想要调用父类的同名和属性， 属性在init初始化位置
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

# 徒孙类
#1.创建类Tusun,用这个类创建对象，2.用这个对象调用父类的属性，看能否成功
class Tusun(Prentic):
    pass

#3.创建对象，验证结论

Peter = Tusun()
Peter.make_cake()
Peter.make_master_cake()
Peter.make_school_cake()

# 拓展  查看类的关系
#print(Prentic.__mro__)