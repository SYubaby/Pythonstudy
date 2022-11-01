''''
高阶函数
把函数作为参数传入

reduce(func, lst), 其中func 必须有两个参数。每次func计算的结果继续和序列的下一个元素做累积计算

需求 计算list1序列中各个数字的累加和
'''


#1. 导入模块
import functools
# 1.准备列表数据
list1 = [1, 2, 3, 4, 5]

#2.
def func(a, b):
    return a + b

#3. 调用reduce
result = functools.reduce(func, list1)

print(result)









