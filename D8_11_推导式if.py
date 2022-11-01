"""
8.列表推导式
字典推导式
集合推导式
简化代码

1.1 创建空列表
1.2 循环将有规律的数据写入到列表

"""


#1. range
list1 = [i for i in range(0, 10, 2)]
print(list1)

#2. for 循环加if 创建有规律的列表
list2 = []
for i in range(10):
    if i % 2 == 0:
        list2.append(i)

print(list2)

#3. 把for循环配合if 的代码
list3 = [i for i in range(10) if i % 2 == 0]
print(list3)
