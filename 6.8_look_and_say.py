def get_next_num(num):
    """ get next number from the given number( in str format ) in a look-and-say sequence """
    ans = []
    i = 0
    while i < len(num):
        j = i
        while j < len(num):
            if num[j] != num[i]:
                break
            j += 1
        ans.extend([str(j-i), num[i]])
        i = j
    return ''.join(ans)


def main():

    n = 3
    vals = ['1']
    val = '1'

    for i in range(1, n):
        vals.append(get_next_num(vals[i-1]))
        val = get_next_num(val)

    print(vals)
    print(val)


if __name__ == '__main__':
    main()



