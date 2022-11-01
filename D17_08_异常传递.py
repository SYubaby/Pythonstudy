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
# 1. 尝试只读方式打开test.txt 文件， 文件存在读取内容，不存在提示用户
#2. 读取内容，循环读取，当无内容的时候退出循环，如果用户意外种猪，提示用户已经被意外终止


import time

try:
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        # 在cmd 中ctrl+c 结束终止
        print('程序被终止')
except:
    print('该文件不存在')
