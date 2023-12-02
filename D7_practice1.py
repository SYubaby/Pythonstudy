# 字典示例

# 创建一个字典
phone_book = {"John": "123-456-7890", "Jane": "987-654-3210"}

# 添加新的键值对
phone_book["Bob"] = "555-555-5555"

# 访问字典中的值
print("John's phone number:", phone_book["John"])

# 删除键值对
del phone_book["Jane"]

# 遍历字典
for name, number in phone_book.items():
    print(f"{name}: {number}")

# 集合示例

# 创建一个集合
fruits = {"apple", "banana", "cherry"}

# 添加元素到集合
fruits.add("orange")

# 移除集合中的元素
fruits.remove("banana")

# 遍历集合
for fruit in fruits:
    print(fruit)

# 集合运算示例
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 并集
print(set1 | set2)

# 交集
print(set1 & set2)

# 差集
print(set1 - set2)
