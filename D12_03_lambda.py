''''
lambda 表达式
如果一个函数有一个 返回值，并且只有一句代码，可以用lambda 简化

lambda 参数列表：表达式
lambda 表达式的参数可有可无，函数的参数在lambda表达式中完全适用
lambda 表达式能接收任何数量的参数但只能返回一个表达式的值

函数返回值100
'''
#1.函数
def fn1():
    return 100

result = fn1()
print(result)

#2.lambda 匿名函数

fn2 = lambda: 100

print(fn2)  # 直接打印没有调用， 输出lambda 内存地址

# 100 返回值， 得调用函数 fn2
print(fn2())













