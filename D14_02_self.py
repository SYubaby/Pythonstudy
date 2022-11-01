'''

'''
# 需求 洗衣机 功能 能洗衣服

# 1. 定义洗衣机类
class Washer():

    def wash(self):  # self 指的是调用该函数的对象
        print('能洗衣服')
        print(self)



haier = Washer()
print(haier)
haier.wash()  # 打印对象和打印self 得到的内存相同
