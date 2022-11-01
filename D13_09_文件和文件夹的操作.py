'''
os 模块
1. 导入模块os
2.使用模块内功能

'''

import os

#1. rename():重命名
#os.rename('1.txt', '10.txt')

#2. remove():删除文件
#os.remove('10.txt')

#3. mkdir(文件夹名字):创建文件夹
#os.mkdir('aa')

#4. rmdir():删除文件夹
#os.rmdir('aa')

#5. getcwd: 返回当前文件夹所在目录
#print(os.getcwd())

#6. chdir ：改变目录路径
#os.mkdir('aa')
# 需求  在aa里面创建bb文件夹 1. 切换目录到aa 2创建bb
#os.chdir('aa')
#os.mkdir('bb')

# 7. listdir : 获取某个文件夹下所有文件，返回一个列表
#print(os.listdir())
print(os.listdir('aa'))

# 8. rename() -- 重命名文件夹
# remove 删除文件夹
os.mkdir('bb')
os.rename('bb', 'bbbb')
