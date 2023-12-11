# 字符串基础：索引和切片
text = "Hello, Python!"
print(text[0])        # 'H'
print(text[-1])       # '!'
print(text[7:13])     # 'Python'

# 字符串方法
uppercase_text = text.upper()
lowercase_text = text.lower()
words = text.split()  # 分割字符串为单词列表
stripped_text = text.strip("!")  # 移除字符串两端的特定字符

print(uppercase_text)
print(lowercase_text)
print(words)
print(stripped_text)

# 字符串格式化
name = "Alice"
formatted_string = f"Hello, {name}!"
print(formatted_string)

# 字符串实际应用示例：简单的用户输入解析
user_input = "  COMMAND:Print   "
command = user_input.strip().split(":")[1].lower()
print(f"Executing the command: {command}")
