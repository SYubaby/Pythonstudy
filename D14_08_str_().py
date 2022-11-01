'''
str ， print 的改变 就会打印  从在这个方法中return 的数据
'''

#1 _定义类 带参数的init, 宽度和高度， 实例方法： 电泳实例属性


class Washer():

    #定义_init_,添加实例属性

    def __init__(self):
        self.width = 300


    def __str__(self):
        return '解释说明： 类的说明或对象状态的说明'


haier1 = Washer()
print(haier1)



