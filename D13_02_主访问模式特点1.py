'''
测试目标 主访问模式 r w a
1. 访问模式对文件的影响

2.访问模式对write()的影响

3. 访问模式是否可以省略


'''
# 1. 打开 open(name, mode)
# name: 目标文件名的字符串 （可以包含文件所在的具体路径
# mode: 设置打开文件的模式（访问模式）：只读，写入，追加等

# r 如果文件不存在，报错:不支持写入操作，表示只读
# f = open('test.text1', 'r')
# f = open('test', 'r')
# f.write('aa')
# f.close()


# w: 只写，如果文件不存在，新建文件夹：执行写入，会覆盖原有内容
# f = open('1.txt', 'w')
# f.write('bbb')
# f.close()

#a: 追加， 如果文件不存在,新建文件夹: 在原有内容基础上追加新内容
f = open('2.txt', 'a')
f.write('xyz')
f.close()

# f访问模式是否可以省略, 可以省略，如果省略表示访问模式为r
# f = open('100.txt')
# f.close() #报错， 没有

f = open('1.txt')
f.close()





