import random


def get_subset(n, k):
    """ select subset of size k from 0,1,2....., n-1 such that the set is equally probable"""
    nums = list(range(n))
    for i in range(k):
        idx = random.randint(i, n-1)
        nums[idx], nums[i] = nums[i], nums[idx]
    return nums[:k]


def get_subset2(n, k):
    """ same algo as above dut diff implementation to reduce space """
    rem_hash = {}
    val_hash = {}
    for i in range(k):
        idx = random.randint(i, n-1)
        val_hash[i] = rem_hash.get(idx, idx)
        rem_hash[idx] = rem_hash.get(i, i)
    return list(val_hash.values())


def main():
    subset = get_subset2(100, 4)
    print(subset)


if __name__ == '__main__':
    main()
