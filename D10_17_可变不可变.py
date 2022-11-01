
'''
可变：
list
dict
set
不可变
int
float
string
tuple
'''

def test1(a):
    print(a)
    print(id(a))

    a += a
    print(a)
    print(id(a))
# 1. 计算前后ID值不同

b = 100
test1(b)


# 2. list 计算前后id值相同
c = [11, 22]

test1(c)








