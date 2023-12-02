# 列表示例

# 创建一个列表
fruits = ["apple", "banana", "cherry"]

# 访问列表元素
print(fruits[0])  # 输出第一个元素 'apple'

# 添加元素到列表末尾
fruits.append("orange")

# 移除列表中的元素
fruits.remove("banana")

# 对列表进行排序
fruits.sort()

# 打印最终列表
print(fruits)  # 输出排序后的列表

# 元组示例

# 创建一个元组
numbers = (1, 2, 3)

# 访问元组元素
print(numbers[1])  # 输出 '2'

# 尝试修改元组（会出错，因为元组是不可变的）
# numbers[1] = 10  # 这将引发错误

# 使用元组中的值
for number in numbers:
    print(number)  # 打印元组中的每个数字
