"""
Set 集合 2.2 删除数据 remove discard pop

"""

s1 = {10, 20, 30, 40, 50}
# remove(): 删除指定数据， 如果数据不存在报错
s1.remove(10)
print(s1)
#s1.remove(10) 报错


# discard()：删除指定数据，如果数据不存在不报错
s1.discard(10)
print(s1)

#pop(): 随机删除某个数据，并返回这个数据
del_num = s1.pop()
print(del_num)
print(s1)
