"""
while
1.打印一个星星
2.一行5个，循环
3. 循环5行星星

"""
# 准备数据
j = 0
while j < 5:
    # 一行星星开始
    i = 0
    # print(i)
    while i < 5:
        print('*', end='') #取消\n
        i += 1
    #一行星星结束，换行显示下一行
    print()
    j += 1
