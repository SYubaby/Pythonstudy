# Comparison operator and logical operator



'''
比较运算符
==
！=
>
<
>=
<=

逻辑运算符
logical operator
and
or
not
datatype: bool
Bracket: Better for complex environment
'''
a = 0
b = 1
c = 2

#1. and: Both true
print(a < b) and (c > b)  # 加小括号 避免歧义
print((a > b) and (c > b))

#2. or: 一真则真，都假才假
print(a < b or c > b)
print(a > b or c > b)

#3. not:
print(not False)
print(not (c > b))

# and,只要有一个值为0，结果为0。否则结果为最后一个非0数字
print(a and b)
print(b and c)

# or，只有所有值为0结果才为0，否则结果为第一个非0数字
print(a or b)
print(b or c)
