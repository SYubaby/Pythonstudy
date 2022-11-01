'''
需求1： 批量修改文件名，即可添加指定字符串，又能删除指定字符串
步骤
需求2： 删除python重名
'''
import os

flag = 2
#1. 设置添加删除字符串的标识： 找到所有文件：获取code文件夹的目录列表 -- listdir()

file_list = os.listdir()
print(file_list)


#2. 构造名字
for i in file_list:
    if flag == 1:
    # new_ name = 'python_' + 原文件i
        new_name = 'Python' + i
    elif flag == 2:
        #删除前缀
        num = len('Python')
        new_name = i[num:]
#3. os.rename()重命名
    os.rename(i, new_name)