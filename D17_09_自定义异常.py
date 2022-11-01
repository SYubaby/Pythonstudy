'''
自定义异常
'''
#自定义异常类，继承Exception

#1. 自定义异常
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len
    #设置抛出异常的描述信息
    def __str__(self):
        return f'输入的是{self.length}， 不能少于{self.min_len}个字符'

def main():
    # 2.给出异常
    try:
        password = input('请输入密码')
        if len(password) < 3:
            #抛出异常类创建对象
            raise ShortInputError(len(password), 3)
    #3. 捕获异常
    except Exception as result:
        print(result)
    else:
        print('密码已经输入完成')

main()



#3.捕获异常
