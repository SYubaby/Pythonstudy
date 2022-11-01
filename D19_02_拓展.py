'''
学员
管理系统

一个部分一个程序文件
项目主程序入口一个文件

'''
#1.定义类
class A(object):
    a= 0

    def __init__(self):
        self.b = 1

#2.创建对象
aa = A()
#3. 调用dict

print(A.__dict__)  # 返回类内部所有属性和方法对应的字典
print(aa.__dict__) # 当前对象的实例属性和值组成的字典



