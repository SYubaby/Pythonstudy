''''
lambda 表达式
如果一个函数有一个 返回值，并且只有一句代码，可以用lambda 简化

lambda 参数列表：表达式
lambda 表达式的参数可有可无，函数的参数在lambda表达式中完全适用
lambda 表达式能接收任何数量的参数但只能返回一个表达式的值

lambda

'''
# 列表数据按字典key 的值排序

students = [{'name': 'Tom', 'age': 20},
            {'name': 'Rose', 'age': 19},
            {'name': 'Jack', 'age': 22}]

# 按name 值升序排列 sort(key=lambda ---, reverse = bool)
students.sort(key=lambda x: x['name'])
print(students)
# 按name 值降序排列
students.sort(key=lambda x: x['name'], reverse=True)
print(students)
# 按age 值升序排序
students.sort(key=lambda x: x['age'])
print(students)











