'''

'''
# 1.一个类可以创建多个对象

class Washer():

    def wash(self):  # self 指的是调用该函数的对象
        print('能洗衣服')
        print(self)

#2. 多个对象都调用函数的时候self 地址是否相同. 地址不相同

haier1 = Washer()
haier1.wash()

haier2 = Washer()
haier2.wash()
