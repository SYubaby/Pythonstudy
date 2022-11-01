"""
key值查找
print(dict1[])
get

"""
dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

#1.[key]
#print(dict1['name'])  #返回对应的值（key值存在 ）
#print(dict1['names']) #报错

#2. 函数 get keys values items 4个函数
#2.1 get()
#print(dict1.get('name')) # TOM
#print(dict1.get('id', 110)) # 110 .  当前查找的key 不存在则返回第二个参数110
#print(dict1.get('id'))  # None 如果key不存在，返回None. 无法赋值

#2.2 keys() 查找字典所有的key,返回可迭代对象。就是可以用for遍历的对象
print(dict1.keys())  # dict_keys(['name', 'age', 'gender'])

#2.3 values 查找所有values 返回的是key的值。返回可迭代对象。
print(dict1.values())  # dict_values([['TOM', 20, '男']])

#2.4。 items 查找字典中所有的键值对， 返回可迭代对象， 里面的数据是元组， 元组数据1 是字典的key, 元组数据2 是字典key对应的值。
print(dict1.items())  # dict_items([('name', 'TOM'), ('age', 20), ('gender', '男')])





