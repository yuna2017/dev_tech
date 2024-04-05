def sum_of_three_numbers():
    a = float(input("请输入第一个数："))
    b = float(input("请输入第二个数："))
    c = float(input("请输入第三个数："))
    return a, b, c

def average_of_three_numbers(a, b, c):
    s = a + b + c
    avg = s / 3
    return avg

if __name__ == '__main__':
    a, b, c = sum_of_three_numbers()
    print("三个数的和为：", a + b + c)
    print("三个数的平均数为：", average_of_three_numbers(a, b, c))
