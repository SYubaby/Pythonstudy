"""
存储数据；student.data
加载文件数据
修改数据后保存到文件
存储数据的形式：列表

系统功能循环使用，用户输入不同功能的序号
"""
from student import *
class StudentManage(object):

    def __init__(self):
        # 存储所用的列表
        self.student_list = []

# 一. 程序入口函数
    def run(self):
        #1.加载学员的信息
        self.load_student()

        while True:
            # 2. 显示功能菜单
            self.show_menu()
            # 3.用户输入目标功能序号
            menu_num = int(input('请输入您需要的功能: '))
            #4. 根据用户输入的序号系统执行不同的功能 -- 1
            if menu_num == 1:
                #添加学员
                self.add_student()
            elif menu_num == 2:
                #删除学员
                self.del_student()
            elif menu_num == 3:
                #修改学员
                self.modify_student()
            elif menu_num == 4:
                #查询学员信息
                self.search_student()
            elif menu_num == 5:
                #显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                #保存学员信息
                self.save_student()
            elif menu_num == 7:
                # 退出系统
                break

    #二。 系统功能函数
    #2.1 显示功能菜单 -- 打印序号的功能对应关系 -- 静态
    @staticmethod
    def show_menu():
        print('请选择如下功能：')
        print('1. 添加学员')
        print('2. 删除学员')
        print('3. 修改学员信息')
        print('4. 查询学员信息')
        print('5. 显示所有学员信息')
        print('6. 保存学员信息')
        print('7. 退出系统')
    #2.2 添加学员
    def add_student(self):
        #1. 用户输入姓名 性别 手机号
        name = input('请输入您的姓名：')
        gender = input('请输入您的性别：')
        tel = input('请输入您的手机号：')

        #2. 创建学员对象：- 类？ 类在student 文件
        student = Student(name, gender, tel)
        #3. 将该对象添加到学员列表：
        self.student_list.append(student)

        # print(self.student_list)
        # print(student)

    #2.3 删除学员
    def del_student(self):
        # print('删除学员')
        #1.用户输入学员姓名
        del_name = input('请输入要删除的学员姓名')
        #2. 遍历学员列表，如果用户输入的学员信息存在删除，不存在提示
        for i in self.student_list:
            if del_name == i.name:
                self.student_list.remove(i)
                break
        else:
            print('查无此人')
        #Test
        # print(self.student_list)

    #2.4 修改学员信息
    def modify_student(self):
        # print('修改学员信息')
        #1. 用户输入姓名
        modify_name = input('请输入要修改的学员姓名：')
        for i in self.student_list:
            if modify_name == i.name:
                i.name = input('姓名：')
                i.gender = input('性别：')
                i.tel = input('电话：')
                print(f'修改成功姓名{i.name}, 性别{i.gender},电话{i.tel}')
                break
        else:
            print('查无此人')

    #2.5 查询学员信息
    def search_student(self):
        # print('查询学员信息')
        #1.
        search_name = input('请输入要查询的学员的姓名')
        #2.
        for i in self.student_list:
            if search_name == i.name:
                print(f'姓名{i.name},性别{i.gender},电话{i.tel}')
                break
        else:
            print('查无此人')
    #2.6 显示所有学员信息
    def show_student(self):
        #1.打印表头
        print('姓名\t性别\t电话')
        #
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    #2.7 保存学员信息
    def save_student(self):
        # print('保存学员信息')
        #1.打开文件
        f = open('student.data', 'w')
        #2.写入数据 列表里面套字典
        #注意1：文件写入的数据不能是学员对象的地址内存，需要把学员数据转换成列表字典数据再做存储
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)

        # 注意2：文件内数据要求为字符串类型，故需要先转换数据类型为字符串才能文件写入数据
        f.write(str(new_list))
        #3.关闭文件
        f.close()

    #2.8 加载学员信息
    def load_student(self):
        # print('加载学员信息')
        #1. 打开文件
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            # 2 .读取数据，读出来字符串，还原成字典  [{}] 转换[学员对象]
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            f.close()


