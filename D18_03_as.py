'''
import 模块名 as 别名
'''
import time as t  # 不能再使用time
t.sleep(2)
print('hello')

from time import sleep as sl
sl(2)
print('hello')



