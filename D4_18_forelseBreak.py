"""
for else: break an

str1 = 'itheima'd continue
for 临时变量 in 序列  -- 临时变量
    重复执行的代码
else:
    循环正常结束
1. 书写道歉的循环
2.循环正常结束要执行的代码 -- else
"""
str1 = 'itheima'

for i in str1:
    if i == 'e':
        print('不打e')
        #break
        continue
    print(i)
else:
    print('循环正常执行')