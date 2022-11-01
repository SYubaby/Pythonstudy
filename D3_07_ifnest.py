"""
Require:
    如果有钱可以上车，没钱不能上车
    上车有空座，可以坐下，没空座，站着
    Nest
"""

"""
Step:
    1.准备判断数据：钱和空座 -- convert datatype from string to int
    2. 判断是否有钱： 上车和 不能上车
    3. 上车了: 判断是否能坐下： 有空座位 和 无空座位
"""

money = 0
seat = 1

if money == 1:
    print('土豪请上车')

    if seat == 1:
        print('给爷坐')
    else:
        print('站着等')
else:
    print('没钱不能上车')

