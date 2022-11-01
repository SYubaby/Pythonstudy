"""
Replace split join
字符串序列.replace(旧子串，新子串，替换次数)

"""
mystr = 'hello world and itcast and itheima and python'

# 1. replace(): change and to he
#new_str = mystr.replace('and','he')
#new_str = mystr.replace('and','he', 1)
new_str = mystr.replace('and','he', 10)

print(mystr)
print(mystr.replace('and', 'he'))
print(new_str)

# 原有字符串数据并没有做到修改，修改后的数据是replace函数的返回值
# 字符串是不可变数据类型
# 数据是否可以划分 分为可变类型 和 不可变类型

#2. split() -- 分割，返回一个列表,丢失分割字符
#list1 = mystr.split('and')
list1 = mystr.split('and', 2)
print(list1)



# 3. join() 用一个字符或子串合并字符串，多个合并成一个
mylist = ['aa', 'bb', 'cc']
newstr = '...'.join(mylist)
print(newstr)


