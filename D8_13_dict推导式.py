"""
8.
字典推导式
集合推导式
简化代码


"""
# 创建一个字典：字典key是1-5数字，value是这个数字的2次方
dict1 = {i: i**2 for i in range(1, 5)}
print(dict1)

# 多for 推导式 = for 循环嵌套
