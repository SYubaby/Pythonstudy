'''
__del__ ， 默认，自动调用
'''

#1 _定义类 带参数的init, 宽度和高度， 实例方法： 电泳实例属性


class Washer():

    #定义_init_,添加实例属性

    def __init__(self):
        self.width = 300


    def __del__(self):
        print(f'对象删除')


haier1 = Washer()




