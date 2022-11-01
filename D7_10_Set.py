"""
Set 集合

"""
#1. 创建有数据的集合 没有顺序所以不支持小标
s1 = {10, 20, 30, 40, 50}
print(s1)

s2 = {10, 30, 30, 40, 50}
print(s2)

s3 = set('abcdefg')
print(s3)
#2. 创建空集合: set()
s4 = set()
print(s4)
print(type(s4))

s5 = {} # 创建的是空字典
print(type(s5))

