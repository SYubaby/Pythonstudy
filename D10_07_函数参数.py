
'''
函数的参数： 4种

位置参数 ： 调用函数时根据函数定义的参数位置来传递参数

关键字参数

缺省参数

不定长参数
'''

def user_info(name, age, gender):
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')



user_info('Tom', 20, '男')

# user_info('Tom', 20) #报错， 定义传入不一致会报错，
# 顺序不一致，导致数据无意义



