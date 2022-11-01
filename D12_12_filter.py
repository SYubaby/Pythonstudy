''''
高阶函数
把函数作为参数传入

filter(func, lst), 函数用于过滤序列。过滤掉不符合条件的元素，返回一个filter对象，
如果要转换为列表，可以用list（）来转换

'''
#1. 导入模块
import functools
# 1.准备列表数据
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#2. 
def func(x):
    return x % 2 == 0


#3. 调用reduce
result = filter(func, list1)

print(result)
print(list(result))
print(set(result))  # no data









