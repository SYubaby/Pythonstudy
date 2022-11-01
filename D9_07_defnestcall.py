
'''
函数嵌套调用
'''
def testB():
    print('B函数开始---')
    print('B 函数')
    print('B函数结束---')

def testA():
    print('A start ---')
    # nest and call B
    testB()
    print('A end ---')

testA()

