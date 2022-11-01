''''
高阶函数
把函数作为参数传入

map(func, lst), 将传入的函数变量func 作用到lst 变量的每个元素中，并将结果组成新的列表

需求 计算list1序列中各个数字的2次方
'''
# 
# 1.准备列表数据
list1 = [1, 2, 3, 4, 5]

#2.准备2次方计算的函数
def func(x):
    return x**2

#3. 调用map
result = map(func, list1)

#4.验收成果
print(result)
print(list(result))








