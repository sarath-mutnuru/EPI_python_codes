def reverse_bits(num):
    """ return the number corresponding to reverse of bit repr. of num """
    ans = 0
    n = num
    num_bin = ''  # the binary str of given num
    ans_bin = ''  # the binary str of resulting num
    while num:
        num_bin = str(num % 2) + num_bin
        ans_bin += str(num % 2)
        ans = ans * 2 + num % 2
        num //= 2
    return n, num_bin, ans, ans_bin


def reverse_bits2(num):
    K = 2 ** 16
    if num < K:
        return reverse_bits(num)
    s1 = reverse_bits(num & 0xff)
    s2 = reverse_bits(num >> 16 & 0xff)
    s3 = reverse_bits(num >> 32 & 0xff)
    s4 = reverse_bits(num >> 48 & 0xff)

    ans_bin = s1[-1] + s2[-1] + s3[-1] + s4[-1]
    ans = s4[2] * 1 + s3[2] * K + s2[2] * (K**2) + s1[2] * (K**3)
    num_bin = s4[1] + s3[1] + s2[1] + s1[1]
    n = s1[0] * 1 + s2[0] * K + s3[0] * (K**2) + s4[0] * (K**3)

    assert(n == num)
    return n, num_bin, ans, ans_bin


def main():
    num = 2**17 + 22
    print('The bin of {0} is {1} and reversed bin is {3} and its decimal is {2}'.format(*reverse_bits2(num)))


if __name__ == '__main__':
    main()