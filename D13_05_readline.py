'''
测试目标 主访问模式 r w a


readlines 按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
'''

f = open('test.text')

content = f.readline()
print(f'第一行：{content}')

content = f.readline()
print(f'第二行：{content}')
f.close()

