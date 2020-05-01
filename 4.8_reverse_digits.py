def reverse(num):
    """ brute force """
    digs = []
    s = 1 if num > 0 else -1
    num = abs(num)
    while num:
        digs.append(num % 10)
        num = num//10  # int type
    res = 0
    fac = 1
    for d in digs[::-1]:
        res += d * fac
        fac *= 10
    return s * res


def reverse2(num):
    """ brute force """
    ans = 0
    s = 1 if num > 0 else -1
    num = abs(num)
    while num:
        ans = ans * 10 + num % 10
        num //= 10
    return s * ans


def main():
    num = -100232
    print('number = {}, reversed number = {}'.format(num, reverse(num)))


if __name__ == '__main__':
    main()



