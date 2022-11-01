'''
了解异常
捕获异常
异常的else
异常finally
异常的传递
自定义异常

try
可能发生错误的代码
except
如果出现异常执行的代码

'''
#Exception是程序异常类的父类

try:
    print(num)
    print(1/0)
except Exception as result:       #异常类型 与 捕获异常不一致则不执行
    print(result)

# Zerodivisionerror
#print(1/0)