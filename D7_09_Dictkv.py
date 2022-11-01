"""
4.1 -4.4

xx. items() : 返回可迭代对象，内部是元组，元组有两个数据

"""
#4.4
dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

for key, value in dict1.items():
    print(f'{key} = {value}')  #目标： key = value
    print(key)
    print(value)


