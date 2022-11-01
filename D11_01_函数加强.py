
'''
学员管理系统
递归
lambda 表达式
高阶函数

Example 学员管理系统：
#需求：1.添加学员：
        存储所有学员信息应该是一个全局变量，数据类型为列表
        # 需求：（1）.接收学员信息，并保存。
        #（2）.判断是否添加学员信息：已经存在，报错； 不存在，则准备空字典，将用户输入的数据追加到字典，再列表追加字典数据
        #（3）. 对应if 条件成立的位置调用该函数

#2. 删除学员：
        (1) 用户输入目标学员姓名
        (2)检查这个学员是否存在
           存在，则列表删除这个数据
           不存在，则提示“不存在”
        (3)对应的if条件成立的位置调用该函数

#3.修改学员信息:
    （1）用户输入目标学员姓名
    （2）检查这个学员是否存在
        存在，则修改这位学员的信息，例如手机号
        不存在，报错
    （3）对应的if条件成立的位置调用该函数

#4.查询学员信息:
    (1)用户输入目标学员姓名
    (2)检查这个学员是否存在
        存在，则显示这位学员的信息，
        不存在，报错
    (3)对应的if条件成立的位置调用该函数
#5. 显示所有学员信息:
    (1)print all information
    (3)对应的if条件成立的位置调用该函数

#6.退出系统:

#系统共有6个功能，用户根据自己的需求选取
'''


#定义功能界面函数
def info_print():
    print('请选择功能---')
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员')
    print('4.查询学员')
    print('5.显示所有学员')
    print('6.退出系统')
    print('-'*20)

#等待存储所有学员信息
info = []

# 添加学员函数 ：
def add_info():
    """添加学员函数"""
    #接收学员信息,1.用户输入学号，姓名，手机号
    new_id = input('请输入学号:')
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')

    #2. 判断是否添加这个学员：存在，报错提示； 不存在，添加数据
    global info
    #2.1 不允许姓名重复：判断用户输入的姓名和列表里面字典的name对应的值相等提示
    for i in info:
        if new_name == i['name']:
            print('此用户已经存在')
            #如果没有return，会重复添加，没有跳出函数。return使后面添加信息不执行
            return
    #2.2 如果不存在添加：准备空字典，字典新增数据，列表追加字典
    info_dict = {}

    #字典新增数据
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    #print(info_dict)

    #列表追加字典
    info.append(info_dict)
    print(info)

#删除学员：
def del_info():
    """删除学员"""
    #1. 用户输入要删除的学员的姓名
    del_name = input('请输入要删除的学员的姓名：')
    #2.判断学员是否存在：存在则删除，不存在提示
    #2.1 声明info 是全局变量
    global info
    #2.2遍历列表
    for i in info:
            # 2.3 判断学员是否存在：存在执行删除列表里面的字典。break：这个系统不允许重名，删除了一个后面的不需要再遍历
            if del_name == i['name']:
                #列表删除数据--按数据删除remove
                info.remove(i)
                break
    else:
        print('该学员不存在')
    print(info)

#修改学员信息：
def modify_info():
    """修改函数"""
    #1. 用户输入要修改的学员的姓名
    modify_name = input('请输入要修改的学员的姓名：')
    #2. 判断是否存在，存在修改手机号，不存在提示
    #2.1 声明info是全局变量
    global info
    #2.2 遍历列表，判断输入的姓名 == 字典['name']
    for i in info:
        if modify_name == i['name']:
            # 将tel 这个key修改，并终止
            i['tel'] = input('请输入新的手机号：')
            break
    else:  #for 跑完以后，同一级别else
        #学员不存在，
        print('该学员不存在')
    #3.打印info
    print(info)

#查询学员信息：
def search_info():
    """查询学员信息"""
    # 1. 用户输入要修改的学员的姓名
    search_name = input('请输入学员姓名：')
    #2. 判断是否存在，存在打印学员信息，不存在提示
    #2.1 声明info是全局变量
    global info
    #2.2 遍历列表，判断输入的姓名 == 字典['name']
    for i in info:
        if search_name == i['name']:
            #学员存在：打印信息并终止循环
            print('查找到的学员信息如下：')
            print(f"该学生的学号是{i['id']}, 姓名是{i['name']}, 手机号是{i['tel']}") #外层用双引号，里面用单引号，否则无法区分
            break
    else:  #for 跑完以后，同一级别else
        #学员不存在，
        print('该学员不存在')
    #3.打印info
    print(info)


#显示所用学员信息
def print_all():
    """显示所有学员信息"""
    #\t 对其
    print('学号\t姓名\t手机号')
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")

# 系统功能需要循环使用,直到用户输入6，才退出系统
while True:
    #1. 显示功能界面（上面6步）
    info_print()
    #2. 用户输入功能序号
    user_num = int(input('请输入功能序号:'))
    #3. 根据输入，执行不同的功能，调用函数
    if user_num == 1:
        #print('添加')
        add_info()
    elif user_num == 2:
        #print('删除')
        del_info()
    elif user_num == 3:
        #print('修改')
        modify_info()
    elif user_num == 4:
        #print('查询')
        search_info()
    elif user_num == 5:
        #print('显示所有学员')
        print_all()
    elif user_num == 6:
        #print('退出系统')
        exit_flag = input('确定要退出吗? yes or no: ')
        if exit_flag == 'yes':
            break
    else:
        print('输入的序号有误')








