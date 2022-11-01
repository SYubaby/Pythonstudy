
'''
返回值作为参数传递

'''

# 定义两个函数，函数2把返回值50 作为参数传入（函数2有形参


def testA():
    return 50

def testB(num):
    print(num)

# 先得到函数1 的返回值（保存函数一的值到一个变量）， 再把返回值传入函数2
result = testA()

#将函数返回值作为变量传递
testB(result)





