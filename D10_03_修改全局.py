
'''
变量作用域，
局部变量：定义在函数体内部的变量，只在函数体内部生效。 函数体内部临时保存数据，
    函数调用完成后，则销毁局部变量

全局变量：在函数体内部，外部都能生效的变量
（要在不同的地方使用）

'''

# 定义全局变量a, 修改为200
a = 100
print(a)
def testA():
    print(a)

def testB():
    # a = 200  #此时的a是局部a,
    # print(a)

    #global 关键字声明a
    global a  # 声明a为全局变量
    a = 200
    print(a)


#都能访问
testA()
testB()
print(a)
print(f'全局变量a = {a}')




