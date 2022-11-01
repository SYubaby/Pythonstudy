"""
# Dict 不支持下标，数据以键值对形式，与数据顺序没有关系
符号 大括号  还有集合
数据为键值对  K V
各个键值对之间用逗号隔开

字典序列【key】 = 值
"""
#新增ID 的值是110
dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

dict1['id'] = 110
print(dict1)
print(type(dict1))

dict1['name'] = 'Rose'
print(dict1)


