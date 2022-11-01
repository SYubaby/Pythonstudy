
'''
运算符
算数运算符
赋值运算符
复合赋值
比较运算符
逻辑运算符
Arithmetic operator
()
** 指数
*
/
// 整除
% 取余
+ -

Assign operator
=
+=
-=

Comparison operator
==
>=
<=
!= 不等于
'''
#  c += a 等价于 c = c+a
#  c %= a 等价于 c = c//a 取余
#
a = 10
a += 1  # a = a + 1
print(a)

b = 10
b -= 1 # b = b - 1
print(b)

# 先算复合运算符右面的然后统一算
c = 10
c += 1 + 2
print(c)

d = 10
d *= 1 + 2
print(d)





