'''
符合标识符命名规则

'''
#import os
#1. rename():重命名
#os.rename('D18_04_制作module.py', 'D18_04_my_module1.py')

def testA(a, b):
    print(a + b)

#测试信息， 如果不被导入
#testA(3,5)


#模块标识符，如果是自身模块print出来是__main__， 如果不是是这个文件名，见调用模块
# print(__name__)  # __name__系统变量

if __name__ == 'main':
    testA(1, 1)
