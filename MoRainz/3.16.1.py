def S(a, b, c):
    return a + b + c


def A(a, b, c):
    sum = S(a, b, c)
    return sum / 3


a = int(input("Enter a number: "))
b = int(input("enter another number: "))
c = int(input("enter another another number: "))
print(S(a, b, c),
      A(a, b, c))
