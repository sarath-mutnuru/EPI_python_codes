def arrange(v):
    """ func to move all even numbers to left and odd to right in place"""

    ev = -1
    od = len(v)
    un = 0

    while ev < od - 1:
        if v[un] % 2 == 0:
            ev += 1
            un += 1
        else:
            v[od - 1], v[un] = v[un], v[od - 1]
            od -= 1


def main():
    v = [1,3,5,7,9]
    print("before arranging : ", v)
    arrange(v)
    print("after arranging : ", v)


if __name__ == '__main__':
    main()