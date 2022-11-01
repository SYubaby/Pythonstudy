"""
需求： 注册邮箱， 用户输入账号名，判断这个账号是否存在,如果存在，提示用户，否则可以注册
1. 用户账号
2.判断if else


"""
name_list = ['TOM', 'Lily', 'Rose']

name = input('请输入您的账号：')

if name in name_list:
    print(f'您输入的名字是{name}, 此用户名已经存在')
else:
    print(f'您输入的名字是{name},可以注册')