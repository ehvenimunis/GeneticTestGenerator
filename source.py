def experiment_code3(a, b, c, d, x):
    var6 = 2
    if (a * var6 + 3 * var6 / var6) == (b + c + d + 7):
        print("*" * 6)
        if b == 10:
            print("#" * 20)
            if d == (10 + 2 * x - 5):
                print("~" * 20)
            else:
                print("@" * 20)
        else:
            print("$" * 20)
    else:
        print("%" * 20)
    return a, b, c, d, x


def experiment_code2(a, b, c, d, x, y):
    if a == b:
        print("**********")
        if b == c:
            print("**********")
            if c == d:
                print("**********")
                if d == x:
                    print("**********")
                    if x == y:
                        print("**********")
                    else:
                        print("sum")
                else:
                    print("**********")
            else:
                print("**********")
        else:
            print("**********")
    else:
        print("**********")
    return a, b, c, d, x, y

def experiment_code1(x, y, z):
    if x != y and x != z and y != z:
        print("scalene triangle")
    else:
        if x == y and x == z and y == z:
            print("equilateral triangle")
        else:
            print("isosceles triangle")
    return x, y, z
