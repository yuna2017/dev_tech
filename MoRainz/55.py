s = str(input())
l = len(s)
if l <= 20:
    left = (20 - l) // 2
    right = 20 - l - left
    print ('=' * left + s + '=' * right)
elif l > 20:
    print(s.center(20,'='))