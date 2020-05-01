def get_spiral_order_vector(v):
    n_r = len(v)
    n_c = len(v[0])
    t = 0
    b = n_r - 1
    l = 0
    r = n_c - 1

    res = []

    while t <= b and l <= r:
        for i in range(l, r + 1):
            res.append(v[t][i])
        t += 1

        for i in range(t, b + 1):
            res.append(v[i][r])
        r -= 1

        if t <= b:
            for i in range(r, l - 1, -1):
                res.append(v[b][i])
            b -= 1

        if l <= r:
            for i in range(b, t - 1, -1):
                res.append(v[i][l])
            l += 1

    return res


def main():
    v = [[1,2,3],[4,5,6],[7,8,9]]
    #v = [[1,2,3]]
    v =[[1],[2],[3]]

    res = get_spiral_order_vector(v)
    print(res)


if __name__ == '__main__':
    main()