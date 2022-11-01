
'''
返回值作为参数传递

'''

# 需求：一个函数两个返回值

# 只执行第一个return
# def return_num():
#     return 1
#     return 2
#
# result = return_num()
# print(result)  # 1


#一个函数多个返回值的写法：
def return_num():
    # return 1, 2   #返回元组
    # return (10, 20)  # 元组
    # return [100, 200] # list 列表
    return {'name': 'Python', 'age': 30} # dict

result = return_num()
print(result)





