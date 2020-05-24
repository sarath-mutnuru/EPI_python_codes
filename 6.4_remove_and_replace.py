def remove_and_replace(arr):
    """ remove 'b' and replace 'a' with two 'd' s """
    c = sum(map(lambda e: e == 'a', arr))

    for _ in range(c):
        arr.append('-1')

    j = len(arr) - 1
    for i in range(len(arr) - c - 1, -1, -1):
        if arr[i] == 'a':
            arr[j], arr[j-1] = 'd', 'd'
            j -= 2
        else:
            arr[j] = arr[i]
            j -= 1

    idx = 0
    for i in range(len(arr)):
        if arr[i] != 'b':
            arr[idx] = arr[i]
            idx += 1
    for j in range(idx, len(arr)):
        arr[j] = ' '
    return


def main():
    # arr = 'a,a,x1,x2,a,x3,a,a,x4,a,a'.split(',')
    # arr = 'x0,a,a,x1,x2,x3,x4,x5,x6,a,x7,a,a,x8,a,a,x9'.split(',')
    arr = 'x2,x1,b,a,x2,b'.split(',')
    remove_and_replace(arr, len(arr))

    print(arr)


if __name__ == '__main__':
    main()
