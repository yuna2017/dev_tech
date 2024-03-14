def format_string(s):
    if len(s) > 20:
        s = s[:20]
    padding = (20 - len(s)) // 2
    output = f'{"="*padding}{s}{"="*padding}'
    print(output.center(20, '='))
    print(output)
input_string = input("请输入字符串：")
format_string(input_string)