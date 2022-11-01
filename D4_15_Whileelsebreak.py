"""
while else:
while 条件：
    条件成立重复执行的代码
else:
    循环正常结束
1. 书写道歉的循环
2.循环正常结束要执行的代码 -- else
"""

# Reqiure: 重复打印5次媳妇儿，我错了 -- 1 2 3 4 5 -数据表示循环的次数 -- 变量 第一次1， 最后5 or 10 - 完成后执行媳妇儿原谅我了

i = 1
while i <= 5:
    if i == 3:
        break
    print('媳妇儿我错了')
    i += 1
else:
    print('原谅你了') # break执行了, else 下方不执行