def experiment_code1(x, y, z):
    if x != y and x != z and y != z:
        print("scalene triangle")
    else:
        if x == y and x == z and y == z:
            print("equilateral triangle")
        else:
            print("isosceles triangle")
    return x, y, z
