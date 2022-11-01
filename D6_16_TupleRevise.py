# Tuple Find 不支持修改，只支持查找
t1 = ('aa', 'bb', 'cc', 'bb')

#t1[0] = 'aaa' # 报错

t2 = ('aa', 'bb', ['cc', 'dd']) #元组有列表可以修改
print(t2[2])
print(t2[2][0])
t2[2][0] = 'TOM'
print(t2)


