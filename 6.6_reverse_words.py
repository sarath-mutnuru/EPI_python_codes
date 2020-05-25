def reverse_words(s):
    """ reverse the words in a sentence """

    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        right -= 1
        left += 1

    idx = 0

    while idx < len(s):

        j = idx
        while j < len(s) and s[j] != ' '.encode('utf-8')[0]:
            j += 1
        l, r = idx, j - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        idx = j + 1

    return


def main():

    # s = "Alice likes Bob"
    s = " I am great player"
    s = bytearray(s, 'utf-8')
    reverse_words(s)
    print(s)


if __name__ == '__main__':
    main()