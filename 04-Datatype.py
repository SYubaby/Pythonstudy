'''
1. 不同变量存储不同的数据类型
2. 验证这些数据的类型--检测数据类型
'''

# int -- 整型 integer
num1 = 1
# float - 浮点型， 小数
num2 = 1.1
print(type(num1))
print(type(num2))

# str - 字符串 string 特点：带引号 quotation mark
a = 'hello world'
print(type(a))

# bool -- 布尔型： 通常判断使用， 两个取值 True and False
b = True
print(type(b))

# list -- 列表
c = [10, 20, 30]
print(type(c))

# tuple -- 元组
d = (10, 20, 30)
print(type(d))

# set-- 集合
e = {10, 20, 30}
print(type(e))

# dict -- 字典 -- 键值对
f = {'name': 'Peter', 'age': 18}
print(type(f))