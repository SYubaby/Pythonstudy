'''

包 文件夹里面有联系的模块
导入包
方法一import 包名.模块名
包 模块

方法2： 必须在—__init__.py 添加all []
'''
#1 方法1
# import mypackage.my_module1
#
# mypackage.my_module1.info_print1()

"""
from 包名 import
模块名.目标
"""
#2.方法2
from mypackage import *
my_module1.info_print1()


