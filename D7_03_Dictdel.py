"""
# Dict 不支持下标，数据以键值对形式，与数据顺序没有关系
符号 大括号  还有集合
数据为键值对  K V
各个键值对之间用逗号隔开

字典序列【key】 = 值
"""
dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}
#del 删除字典或指定的键值对
#del(dict1)
#print(dict1)

del dict1['name']
print(dict1)

# clear()
dict1.clear()
print(dict1)


