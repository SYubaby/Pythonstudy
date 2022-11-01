''''
高阶函数
把函数作为参数传入

任意两个数字，先进行数字处理（绝对值或四舍五入）再求和计算
'''
# 写法1
def add_num(a, b):
    #绝对值
    return abs(a) + abs(b)


result = add_num(-1.1, 1.9)
print(result)


# 写法2 高阶函数: f是第三个参数，用来接收将来传入的函数
def sum_num(a, b, f):
    return f(a) + f(b)


result1 = sum_num(-1, 5, abs)
print(result1)

result2 = sum_num(-1.1, 5.3, round)
print(result2)











