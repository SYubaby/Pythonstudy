''''
递归
函数内部自己调用自己
必须有出口

3以内数字累加和
'''


# 3+2+1
# 2+1
# 1
# 6 = 3+2以内数字累加和
# 2以内数字累加和 = 2 + 1以内数字累加和
# 1 以内数字累加和 = 1 #出口

def sum_numbers(num):
    # 2. 出口
    if num == 1:
        return 1
    # 1. 当前数字 + 当前数字-1的累加和
    return num + sum_numbers(num-1)

result = sum_numbers(3)  # 1000 超出最大递归深度
print(result)













