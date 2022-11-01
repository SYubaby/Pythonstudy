'''
面向对象三大特性
类属性和实例属性
类方法和静态方法
封装
继承
多态
传入不同的对象，产生不同的结果

'''
# 类属性就是类对象所拥有的属性，它被该类的所有势力对象所共有。
# 类属性可以使用类对象或势力对象访问

# 定义类
class Dog(object):
    tooth= 10

#2.创建对象
wangcai = Dog()
xiaohei = Dog()

#3.访问类属性：类和对象
print(Dog.tooth) # 10
print(wangcai.tooth)
print(xiaohei)