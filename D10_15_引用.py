
'''
了解引用
id()判断两个变量是否为同一个值的引用
'''

# 1. int类型
a = 1

b = a

print(b)

# a 和b 的id 值相同的
print(id(a))
print(id(b))

# 修改a的数据测试id值
a = 2
print(b) #1 int 类型不可变类型

# 因为修改了a的数据，内存要开辟另外一份内存储2，id, a ,b 地址不同
print(id(a))
print(id(b))

# 2. list 可变类型
aa = [10, 20]
bb = aa

print(bb)

print(id(aa))
print(id(bb))

aa.append(30)
print(aa)
print(bb) #列表可变类型

print(id(aa))
print(id(bb))




