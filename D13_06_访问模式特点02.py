'''
测试目标 主访问模式 r w a
1. r+ 和 w+ 区别
r 没有该文件报错


2.文件指针的影响

'''

# r+: 没有该文件报错，文件指针在开头，所以能读取出来数据
# f = open('test.text', 'r+')
# f = open('test1.text', 'r+')


# w+ 没有该文件会新建文件, 文件指针在开头，用新内容覆盖原内容
# f = open('test1.text', 'w+')
# f = open('test.text', 'w+')

#a+ 没有该文件会新建文件，文件指针在结尾，无法读取数据（文件指针后面没有数据）
f = open('test.text', 'a+')
con = f.read()  # 空的
print(con)

f.close()


