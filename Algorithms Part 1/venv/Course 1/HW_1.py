alpha = 3141592653589793238462643383279502884197169399375105820974944592
beta = 2718281828459045235360287471352662497757247093699959574966967627

def divide(x, y):
    if int(x) <= 10 and int(y) <= 10:
        return int(x) * int(y)
    x_length = int(len(str(x)) / 2)
    y_length = int(len(str(y)) / 2)
    a = str(x)[0:x_length]
    b = str(x)[x_length:]
    c = str(y)[0:y_length]
    d = str(y)[y_length:]
    return merge(a, b, c, d)


def merge(a, b, c, d):
    x = len(str(a)) + len(str(b))
    x_mid = int(x/2)
    return 10 ** x * divide(a, c) + 10 ** x_mid * (divide(a, d) + divide(b, c)) + divide(b, d)


print(divide(alpha, beta))
print(alpha*beta)
