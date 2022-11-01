
'''
计算
'''

# 1. 三个数求和
def sum_num(a, b, c):
    return a + b +c

result = sum_num(1, 2, 3)
print(result)

#2. 求平均

def average_num(a, b, c):
    sumResults = sum_num(a, b, c)
    return sumResults/3


ave = average_num(1, 2, 3)
print(ave)

