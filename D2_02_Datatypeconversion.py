'''
1. input
2. Check input data type
3. int () convert data type
4. Check data type
5. Other data type conversion
'''
"""
num = input('请输入数字：') #input 都是字符串类型
print(num)

print(type(num)) #str 都是字符串

int(num)
print(type(int(num)))

"""
#1. float() --
num1 = 1
str1 = '10'
print(type(float(num1)))
print(float(num1)) #1.0
print(float(str1)) #10.0


#2 str() --
print(type(str(num1)))


#3. tuple() -- 将一个序列转换成元组
list1 = [10, 20, 30]
print(tuple(list1))

#4. list() --
t1 = (100, 200, 300)
print(list(t1))

#5. eval () -- 计算字符串中有效python表达式，并返回一个对象。eval 返回他本身的类型
str2 = '1'
str3 = '1.1'
str4 = '(1000, 2000, 3000)'
str5 = '[1000, 2000, 3000]'

print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))
