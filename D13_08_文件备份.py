'''
需求：用户输入当前目录下任意文件名，程序完成对该文件的备份功能

接收用户输入的文件名
规划备份文件名
备份文件写入数据

'''
#1. 接收用户输入目标文件名 sound.txt.mp3
old_name = input('请输入备份文件名：')
# print(old_name)
# print(type(old_name))
#2. 规划备份文件名
#2.1 提取目标文件后缀， 找到名字中的点 -- 名字和后缀分离
index = old_name.rfind('.')

#4. 有效文件才备份 .txt
if index > 0:
    postfix = old_name[index:]
# print(index)

#2.2 组织备份的文件名，xx[备份]后缀 -- 组织新名字 -- 原名字+备份+后缀
#原名字就是字符串中的一部分子串： --  切片[开始：结束：步长]
# print(old_name[:index])
# print(old_name[index:])
# new_name = old_name[:index] + 'copy' + old_name[index:]
new_name = old_name[:index] + 'copy' + postfix

print(new_name)


#3. 备份文件写入数据
#3.1 打开原文件和备份文件 rb 二进制

old_f = open(old_name, 'rb')
new_f = open(new_name, 'wb')

#3.2 原文件读取，备份文件写入
# 如果不确定目标文件大小，循环读取写入，当读取出来的数据没有了终止循环
while True:
    con = old_f.read(1024)
    if len(con) == 0:
        # 表示读取完成了
        break


    new_f.write(con)




#3.3关闭文件
old_f.close()
new_f.close()


