def power(x, y):
    """  return x^y x is double y is int """
    res = 1
    if y < 0:
        x = 1/x
        y = -y

    while y:
        res *= x
        y -= 1
    return res


def power2(x, y):
    if y < 0:
        x = 1/x
        y = -y
    res = 1
    while y:
        if y & 1:
            res = res * x
            y = y-1
        x = x * x
        y = y >> 1
    return res


def main():
    x=3
    y=-3
    print(power2(x,y))
    print(power(x,y))

if __name__ == '__main__':
    main()