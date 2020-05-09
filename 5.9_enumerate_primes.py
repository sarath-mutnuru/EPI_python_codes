def get_primes(N):
    """ enlist all primes b/w 1 to N """

    vec = [1 for _ in range(N+1)]
    for num in range(2, N+1):
        if vec[num] == 1:
            for j in range(num*2, N + 1, num):
                vec[j] = 0
    primes = [x for x in range(1, N + 1) if vec[x]]
    return primes


def main():
    N = 0
    primes = get_primes(N)
    print("Primes b/w 1 and {} are {}".format(N, primes))


if __name__ == '__main__':
    main()
