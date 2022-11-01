# Tuple Find 不支持修改，只支持查找
t1 = ('aa', 'bb', 'cc', 'bb')

#1. 下标
#print(t1[0])

#2. index
#print(t1.index('bb'))
# print(t1.index('bbb')) #报错不存在

#3. count() 统计个数
print(t1.count('bb'))

#4. len() 统计总个数
print(len(t1))

