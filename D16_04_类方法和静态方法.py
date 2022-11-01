'''
面向对象三大特性
类属性和实例属性
类方法和静态方法
封装
继承
多态
传入不同的对象，产生不同的结果

'''
# @classmethod 第一个参数必须是类对象
#方法如果需要使用类对象， 如访问私有类属性等
# 定义类:私有类属性， 类方法获取这个私有类属性
class Dog(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth


#2.创建对象
wangcai = Dog()
result = wangcai.get_tooth()
print(result)

