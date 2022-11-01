"""
8.
字典推导式
提取字典目标数据


"""
counts = {'MBP': 268, 'HP': 125, 'Dell': 201, 'lenovo': 199, 'acer': 99}

# 提取大于等于200的
# 获取所有键值对数据，判断v值大于等于200返回字典
dict1 = {key: value for key, value in counts.items() if value >= 200}

print(dict1)


