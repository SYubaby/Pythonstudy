'''
测试目标 主访问模式 r w a


read
文件对象.read(num) num 单位是字节
'''

f = open('test.text', 'r')

# 文件内容换行，\n 算一个字节，会有字节占位
#read 不写参数表示读取所有
# print(f.read())
print(f.read(10))

f.close()

