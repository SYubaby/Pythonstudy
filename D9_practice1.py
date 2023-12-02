# 函数定义和调用示例

# 定义一个函数
def greet(name):
    """向名为name的人问好"""
    print(f"Hello, {name}!")

# 调用函数
greet("Alice")
greet("Bob")

# 参数和返回值示例

# 定义一个计算平方的函数
def square(number):
    """返回number的平方"""
    return number * number

# 调用函数并使用其返回值
result = square(4)
print("The square of 4 is:", result)

# 组合使用函数

# 定义一个计算平均值的函数
def average(num1, num2):
    """返回num1和num2的平均值"""
    return (num1 + num2) / 2

# 使用函数
avg = average(10, 20)
print("Average of 10 and 20 is:", avg)
