# 输入一个字符串s
s = input("请输入一个字符串：")

# 如果字符串长度超过20，只取前20个字符
if len(s) > 20:
    s = s[:20]

# 确保总宽度为20个字符
padding_length = 20 - len(s)

# 创建等号填充字符串
padding = '=' * (padding_length // 2)

# 输出结果，居中对齐
print(f"{padding}{s}{padding}")
