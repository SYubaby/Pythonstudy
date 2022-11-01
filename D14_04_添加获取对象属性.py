'''
添加获取对象属性
属性=特征  例如高度宽度

可在类外面可里面
对象名.属性名 = 值

'''
class Washer():

    def wash(self):  # self 指的是调用该函数的对象
        print('能洗衣服')

haier1 = Washer()

#添加属性
haier1.width = 400
haier1.length = 500

# 对象名.属性名
print(f'haier1的宽度{haier1.width}')
print(f'haier1的宽度{haier1.length}')



