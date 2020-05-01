def dutch_partition(v, idx):
    """ perform dutch national flag type partition - less, equal, greater with v[idx] as pivot element """
    pvt = v[idx]
    v[idx], v[-1] = v[-1], v[idx]

    st = 0
    en = len(v) - 2

    while st < en:
        if v[st] <= pvt:
            st +=1
        else:
            v[st], v[en] = v[en], v[st]
            en -= 1

    if v[st] <= pvt and st + 1 < len(v):
        v[-1], v[st + 1] = v[st + 1], v[-1]
        pos = st + 1
    else:
        v[-1], v[st] = v[st], v[-1]
        pos = st

    en = pos - 1
    st = 0

    while st < en:
        if v[st] < pvt:
            st += 1
        else:
            v[st], v[en] = v[en], v[st]
            en -= 1

    pvt_end = pos
    if v[st] < pvt:
        pvt_start = st + 1
    else:
        pvt_start = st

    return pvt_start, pvt_end


def main():
    #v = [1, 1, 0, 1, 0, 2, 2, 3, 2]
    v=[0]
    st, en = dutch_partition(v, 0)
    print("The partitioned vector is {}, pivot is {}, pivot start_idx is {}, pivot end_idx is {}"
          .format(v, v[st], st, en))


if __name__ == '__main__':
    main()