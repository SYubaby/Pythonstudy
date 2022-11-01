'''
继承的概念 节省代码，其他慢慢来
单继承
多继承
子类重写父类的同名属性的方法
子类调用父类的同名属性和方法
多层继承
super
私有属性和私有方法

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

#2 徒弟类
#子类B：
class Prentic(Master):
    pass

#3.创建对象，验证结论

result = Prentic()

print(result.kongfu)

result.make_cake()


