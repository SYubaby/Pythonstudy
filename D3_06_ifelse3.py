"""
Require:
    如果年龄小于18，童工，不合法：
    如果年龄18-60岁之间，为合法工作年龄
    如果年龄大于60为退休年龄
"""

"""
Step:
    1.Input age and save variable -- convert datatype from string to int
    2. if 判断 elif
    3. Output age: 您输入的年龄是x,合法与否
"""

age = int(input('请输入您的年龄：'))

# 童工
if age < 18:
    print(f'您输入的年龄是{age}, 童工')

# 18 - 60
elif 18 <= age <= 60:
    print(f'您输入的年龄是{age}, 合法')

# 大于60
elif age > 60:
    print(f'您输入的年龄是{age}, 退休年龄')
