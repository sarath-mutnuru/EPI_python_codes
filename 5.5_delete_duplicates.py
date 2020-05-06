def move(vec, st, en):
    """ move vec[en:len(vec)-1] to v[st]"""
    i = st
    while i <= st + len(vec) - 1 - en:
        vec[i] = vec[i + en - st]
        i += 1


def delete_duplicates(vec):
    """ vec is sorted array, we need to delete the duplicates """

    idx_intervals = []

    i = 0
    nb = 0
    while i < len(vec):
        j = i + 1
        while j < len(vec) and vec[j] == vec[i]:
            j += 1

        if j - 1 > i:
            idx_intervals.append((i, j - 1))
            nb += (j-1-i)

        i = j

    for idx in idx_intervals[::-1]:
        move(vec, idx[0], idx[1])

    for j in range(len(vec) - 1, len(vec) - 1 - nb, -1):
        vec[j] = 0
    return len(vec) - nb


def delete_duplicates2(vec):
    """ vec is sorted array, we need to delete the duplicates """

    i = 0
    nb = 0
    n = len(vec) - 1
    while i <= n:
        j = i + 1
        while j <= n and vec[j] == vec[i]:
            j += 1
        if j - 1 > i:
            nb += (j-1-i)
            move(vec, i, j-1)
            n -= (j-1-i)
        i += 1

    for j in range(len(vec) - 1, len(vec) - 1 - nb, -1):
        vec[j] = 0

    return len(vec) - nb


def delete_duplicates3(vec):

    if not vec:
        return 0
    if len(vec) == 1:
        return 1
    v = 1
    for i in range(len(vec)):
        if vec[v-1] != vec[i]:
            vec[v] = vec[i]
            v  += 1
    return v


def main():
    vec = [1, 1, 1, 2, 3, 4, 4, 5, 7, 8, 8, 8, 8]
    #vec =[0,0]
    i = delete_duplicates3(vec)
    print(i)
    print(vec)


if __name__ == '__main__':
    main()