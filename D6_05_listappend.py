"""
list.append
list.extend
list.insert

"""
name_list = ['TOM', 'Lily', 'Rose']

# 1. append
#name_list.append([11,22])  # 1.列表数据可以更改，列表是可变数据类型：追加到结尾。2.如果append追加的数据是一个序列，则追加整个序列到列表
#print(name_list)

# 2. extend：列表结尾追加数据; 如果追加数据是一个序列，把数据序列里面的数据拆开然后逐一追加到列表的结尾
#name_list.extend('xiaoming')
#name_list.extend(['BB', 'xiaoming'])
#print(name_list)

# 3. insert: 插入在任意位置
name_list.insert(1, 'aaa')
print(name_list)


