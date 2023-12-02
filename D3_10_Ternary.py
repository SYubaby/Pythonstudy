"""
语法:
条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
化简if else 用
"""
a = 3
b = 2

c = a if a > b else b

print(c)

# Reqiure: 有两个变量比较大小
#如果变量1 > 变量2： 执行变量1 - 2； 否则 2 - 1
aa = 10
bb = 6
cc = aa - bb if aa > bb else bb - aa
print(cc)