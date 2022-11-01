"""
8.
字典推导式
将两个列表合并为一个字典


"""
list1 = ['name', 'age', 'gender'] # list1 = ['name', 'age', 'gender', 'id']l 报错， 此时取list2长度
list2 = ['Tom', 20, 'man']

dict1 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict1)

# 总结：
# 两个list 个数相同， len 统计任何一个都可以
# 两个list 个数不同， len 统计少的才能run
