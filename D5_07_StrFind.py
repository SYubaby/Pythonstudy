"""
Find and index

"""
mystr = 'hello world and itcast and itheima and python'

# 1. find
#print(mystr.find('and'))  #12
#print(mystr.find('and', 15, 30))  #23 添加开始结束下标
print(mystr.find('ands'))  #-1 ands  不存在

#2. index

#print(mystr.index('and')) #12
#print(mystr.index('and',15,30))
#print(mystr.index('ands'))  # 报错， index 子串不存在

# 3. count() 次数

print(mystr.count('and', 15, 30)) #1
print(mystr.count('and')) #3
print(mystr.count('ands')) #0

# 4. rfind() 从右侧开始找
print(mystr.rfind('and'))
print(mystr.rfind('ands'))

#5. rindex()
print(mystr.rindex('and'))
print(mystr.rindex('ands'))
