def reverseNumber(x):
    x = int(str(x)[::-1])
    return x

x = 123
y = reverseNumber(x)
print(y)