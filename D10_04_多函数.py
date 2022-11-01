
'''
多函数程序执行流程

共用全局变量

1 声明全局变量
2定义两个函数
3 函数1修改全局变量
函数2 访问全局变量
'''

# 定义全局变量a,
glo_num = 0
print(glo_num)

def testA():
    global glo_num
    glo_num = 100


def testB():
    print(glo_num)


#都能访问
print(glo_num)
testB()
testA()
testB()
print(glo_num)
print(f'全局变量a = {glo_num}')




