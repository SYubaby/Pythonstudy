"""
#要加int 从字符串改成int
"""

age = int(input('请输入您的年龄：')) # input本来接收的是str

if age >= 18:
    print(f'您输入的年龄是{age}, 已经成年，可以上网')
else:
    print(f'您输入的年龄是{age}, 小朋友回家写作业去')

print('系统关闭')