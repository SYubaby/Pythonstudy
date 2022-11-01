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
# 尝试打开test.txt (r), 如果文件不存在

try:
    f = open('test.txt', 'r')
except:
    f = open('test.txt', 'w')