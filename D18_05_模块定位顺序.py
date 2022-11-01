'''
符合标识符命名规则

'''
# 自己文件名不能跟已有模块名重复，如果重复无法使用. #优先搜索当前
# import random
# num = random.randint(1,5)
# print(num)
#2. 使用 from xx import 功能 导入模块的功能的时候，如果功能名字重复，导入的时候定义或后导入的
# from time import sleep
# def sleep():
#   print('自定义的sleep')
#sleep(2)

#拓展：名字重复
#import 模块。 不需要担心功能重名
import time
print(time)
time =1
print(time)

# 为什么变量也能覆盖模块名,数据通过引用传递