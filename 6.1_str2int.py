def str2int(s):
    """ convert string to int -ve numbers included """
    idx, sgn = (1, -1) if '-' == s[0] else (0, 1)
    ans = 0

    for i in range(idx, len(s)):
        ans = ans*10 + int(s[i])

    return ans*sgn


def int2str(num):
    """ convert int to str """
    v = []
    sgn = -1 if num < 0 else 1
    n1 = sgn*num

    while True:
        v.append(n1 % 10)
        n1 //= 10
        if n1 == 0:
            break

    ans = ('-' if sgn == -1 else '') + ''.join(map(str, reversed(v)))

    return ans


def main():
    s = "0"
    print("str is {} and int is {}".format(s, str2int(s)))
    num = -10
    print("int is {} and str is {}".format(num, int2str(num)))


if __name__ == '__main__':
    main()
