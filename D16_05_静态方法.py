'''
面向对象三大特性
类属性和实例属性
类方法和静态方法
封装
继承
多态
传入不同的对象，产生不同的结果

'''
# @staticmethod 静态方法既不需要传递类对象也不需要传递实例对象  形参没有self cls
#也能通过实例对象和类对象访问

#  定义类  定义静态方法
class Dog(object):
    __tooth = 10

    @staticmethod
    def info_print():
        print('狗类')


#2.创建对象
wangcai = Dog()

# 3 调用静态方法  类和对象

wangcai.info_print()
Dog.info_print()
