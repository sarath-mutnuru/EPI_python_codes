def base_conversion(num_str, b_src, b_trg):
    d1 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    d2 = {d1[key]: key for key in d1}

    n = 0
    neg, idx = False, 0
    if num_str[0] == '-':
        neg, idx = True, 1

    for c in num_str[idx:]:
        n = n*b_src + d1.get(c, int(c))

    ans = []
    while True:
        ans.append(d2.get(n % b_trg, n % b_trg))
        n //= b_trg
        if n == 0:
            break

    return ('-' if neg else None) + ''.join(map(str, reversed(ans)))


def main():
    num_str = '-615'
    b_src = 7
    b_trg = 13
    ans = base_conversion(num_str, b_src, b_trg)
    print("src num : {}, src base : {}, trg num : {}, trg base :{}".format(num_str, b_src, ans, b_trg))


if __name__ == '__main__':
    main()