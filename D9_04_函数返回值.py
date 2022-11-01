"""
9
函数返回值作用

return 作用
1.负责函数返回值
2. 退出当前函数，导致return下方的所有代码（函数体内部）不执行
"""
# 1 定义函数，返回烟

def buy():
    return '烟'
    print('ok')

#return 返回结果给函数调用的地方

# 使用变量保存函数返回值
goods = buy()
print(goods)
