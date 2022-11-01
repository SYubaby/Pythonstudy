"""
8. enumerate(对象, start = 0)

 return to 元组
"""
list1 = [10, 20, 30, 20, 40, 50]
s1 = {100, 200, 300, 400, 500}
t1 = ('a', 'b', 'c', 'd', 'e')
#tuple(): 转换成元组
print(tuple(list1))
print(tuple(s1))
#list():转换成列表
print(list(s1))
print(list(t1))
#set():转换成集合
print(set(list1)) #集合有去重功能，不支持下标（没有顺序）
print(set(t1))