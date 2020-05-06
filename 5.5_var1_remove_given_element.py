def remove_element(arr, elem):
    """ remove all occurrences of elem in arr and left shift accordingly """
    idx = 0
    for i in range(len(arr)):
        if arr[i] != elem:
            arr[idx] = arr[i]
            idx += 1
    return idx


def main():
    v = [1, 5, 3, 4, 2, 1, 2, 8, 2, 9]
    elem = 2
    idx = remove_element(v, elem)
    print(idx)
    print("array after removing {} is {}".format(elem, v[:idx]))


if __name__ == '__main__':
    main()