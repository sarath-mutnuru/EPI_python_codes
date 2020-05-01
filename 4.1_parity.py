
def parity(word):
    w = word
    res = 0
    while w:
        res = res ^ (w % 2)
        w = int(w/2)
    return res


def parity2(word):
    if word == 0:
        return 0
    return parity2(word >> 1) ^ (word & 1)


def parity3(word):
    res = 0
    while word:
        res = res ^ (word & 1)
        word = word & (word - 1)  # set least significant set bit to zero.
    return res


def parity4(word):
    m = 2**16 - 1
    if word < m:
        return parity(word)
    cache = [parity(w) for w in range(m+1)]

    ans = cache[word & 0xff] ^ cache[(word >> 16) & 0xff] ^ cache[(word >> 32) & 0xff] ^ cache[(word >> 48) & 0xff]
    # while word:
    #     result = result ^ cache[word % m]
    #     word = int(word/m)
    return ans


def main():
    print(parity(20))
    print(parity2(20))
    print(parity3(20))
    print(parity4(2*54+1))
    return


if __name__ == '__main__':
    main()