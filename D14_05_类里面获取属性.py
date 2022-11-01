'''
添加获取对象属性
属性=特征  例如高度宽度

可在类外面可里面


里面： self.属性名
对象名.属性名 = 值

'''
class Washer():

    def wash(self):
        print('洗衣服')

    def print_info(self):  # self 指的是调用该函数的对象
        #类里面获取实例属性
        print(f'haier1的宽度{self.width}')
        print(f'haier1的宽度{self.length}')

haier1 = Washer()

#添加属性
haier1.width = 400
haier1.length = 500


haier1.print_info()


