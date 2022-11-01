'''

'''
#经典类：class 类名新式类： class 类名（object）

# 默认继承object类， object 是顶级类 或基类，其他子类叫派生类

#1. 师父类
class Master(object):
    def __init__(self):
        # name
        self.kongfu = '[配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


#创建学校类
class School(object):
    def __init__(self):
        # name
        self.kongfu = '[别人配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


#2 徒弟类
#子类B：添加和父类同名的属性和方法
class Prentic(School, Master):
    def __init__(self):
        # name
        self.kongfu = '[自己配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

#3.创建对象，验证结论

result = Prentic()

print(result.kongfu)

result.make_cake()

# 结论：如果子类和父类拥有同名属性和方法，子类创建对象调用属性和方法的时候，调用到的是子类里面的同名属性和方法

# 拓展  查看类的关系
print(Prentic.__mro__)