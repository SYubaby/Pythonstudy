"""
8. enumerate(对象, start = 0)

 return to 元组
"""
list1 = ['a', 'b', 'c', 'd', 'e']

#for i in enumerate(list1):
#    print(i)
#(0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')

#for i in enumerate(list1, start=1):
#    print(i)

for index, char in enumerate(list1, start=1):
    print(f'下标是{index}，对应的字符是{char}')