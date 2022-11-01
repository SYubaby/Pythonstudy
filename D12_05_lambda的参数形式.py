''''
lambda 表达式
如果一个函数有一个 返回值，并且只有一句代码，可以用lambda 简化

lambda 参数列表：表达式
lambda 表达式的参数可有可无，函数的参数在lambda表达式中完全适用
lambda 表达式能接收任何数量的参数但只能返回一个表达式的值

lambda 参数
1 无参数
2.一个参数
3.默认参数
4.可变参数
'''
#无参数

fn1 = lambda: 100

print(fn1())

# 一个参数
fn2 = lambda a: a #验证数据是否传输成功

print(fn2('hello world'))

# 默认参数

fn3 = lambda a, b, c = 100: a + b + c
print(fn3(10, 20))
print(fn3(10, 20, 200))

# 可变参数：*args
fn4 = lambda *args: args
print(fn4(10, 20))
print(fn4(10))

# **kwargs
fn5 = lambda **kwargs: kwargs
print(fn5(name='python'))
print(fn5(name='python', age=30))












