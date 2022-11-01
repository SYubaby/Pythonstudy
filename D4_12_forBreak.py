"""
for 临时变量 in 序列  -- 临时变量
    重复执行的代码
1. 准备数据序列
2. for
"""

str1 = 'itheima'

for i in str1:
    # 当某些条件成立推出循环 -- break: 条件 i 取到e
    if i == 'e':
        print('有e')
        break
    print(i)

