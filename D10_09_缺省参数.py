
'''
函数的参数： 4种

位置参数 ： 调用函数时根据函数定义的参数位置来传递参数

关键字参数： 函数调用，通过键=值形式加以指定，可以让函数更加清晰，容易使用，同时也清楚了参数的顺序需求

缺省参数: 默认参数，用于定义函数，为参数提供默认值，调用函数时，可给默认参数传值或者不传

不定长参数:
'''

def user_info(name, age, gender='男'):
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')



user_info('Tom', 20)

user_info('Peter', 18, gender='女')

user_info('小明', gender='女', age=16) #关键字参数之间不分先后顺序 # 位置参数必须写在关键字参数前面




