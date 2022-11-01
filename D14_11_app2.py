'''
搬家具

需求：
将小于房子剩余面积的家具放到房子中
'''
# 1. 定义类：初始化属性， 房子类 家具类
#家具类
class Furniture():
    def __init__(self, name, area): #形参原因
        # name
        self.name = name
        # area
        self.area = area



class Home():

    def __init__(self, address, area):
        # 地址
        self.address = address
        # 占地面积
        self.area = area
        # 剩余面积
        self.free_area = area
        #家具列表
        self.furniture = []

# 2.显示对象信息
    def __str__(self):
        return f'房子在{self.address}, 面积是{self.area}, 剩余面积{self.free_area}, 家具有{self.furniture}'


    def add_furniture(self, item):
        # 实例方法：容纳家具
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            # 家具搬入后，房屋剩余面积 = 之前剩余面积 - 该家具面积
            self.free_area -= item.area
        else:
            print('家具太大，剩余面积不足，无法容纳')



# 双人床
bed = Furniture('双人床', 6)
sofa = Furniture('沙发', 10)


# 3. 创建对象并调用对应的实例方法
jia1 = Home('北京', 1200)
print(jia1)

jia1.add_furniture(bed)
print(jia1)

jia1.add_furniture(sofa)
print(jia1)

ball = Furniture('test', 1200)
jia1.add_furniture(ball)
print(jia1)