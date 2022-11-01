"""
8.列表推导式
字典推导式
集合推导式
简化代码

1.1 创建空列表
1.2 循环将有规律的数据写入到列表

总结：
#列表推导式： [xx for xx in range()]
#字典推导式： {xx1: xx2 for ... in ...}
#集合推导式： {xx for xx in...}
"""


# while

#1. 准备一个空列表
# list1 = []
# i = 0
# while i < 10:
#     list1.append(i)
#     i += 1
#
# print(list1)

# for ---

# list1 = []
# for i in range (10):
#     list.append(i)
# print(list1)

# 列表推导式
list1 = [i for i in range(10)]
print(list1)