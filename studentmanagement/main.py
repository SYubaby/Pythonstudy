#1. 导入模块
from managersystem import *

#2. 启动管理系统
#保证当前文件运行才启动管理系统
if __name__ == '__main__':

    student_manager = StudentManage()

    student_manager.run()