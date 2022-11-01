"""
8.列表推导式
字典推导式
集合推导式
简化代码

1.1 创建空列表
1.2 循环将有规律的数据写入到列表

"""
# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# Data1: 1 , 2:  range(1,3)
# Data2: 012 range(3)

list1 = []
for i in range(1, 3):
    for j in range(3):
        # list 里面加元组tuple, 循环前准备一个空列表，这里追加元组数据到列表
        list1.append((i, j))

print(list1)

# 多个for 实现列表推导式
list2 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list2)

# 多for 推导式 = for 循环嵌套
