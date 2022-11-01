''''
lambda 表达式
如果一个函数有一个 返回值，并且只有一句代码，可以用lambda 简化

lambda 参数列表：表达式
lambda 表达式的参数可有可无，函数的参数在lambda表达式中完全适用
lambda 表达式能接收任何数量的参数但只能返回一个表达式的值

计算a+b
'''
#1.函数
def add(a, b):
    return a + b

result = add(1, 2)
print(result)

#2.lambda 匿名函数

fn1 = lambda a, b: a + b

print(fn1(1, 2))













