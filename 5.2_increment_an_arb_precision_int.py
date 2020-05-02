import copy


def convert_int_to_arr(num):
    """
    convert an int to an array of digits
    with arr[0] as LSD and arr[-1] as MSD
    """
    res = []
    while num:
        res.append(num % 10)
        num //= 10
    return res


def convert_arr_to_int(arr):
    """
    convert arr of digits with arr[0] as LSD and arr[-1] as MSD to int
    """
    num = 0
    fac = 1
    for d in arr:
        num += d*fac
        fac *= 10
    return num


def increment(nums):

    """
    nums is an array with each entry as a digit and nums[0] as LSD and nums[-1] is MSD
    for eg. 436 is [6,3,4]
    return nums with incremented by 1

    """

    if nums[0] != 9:
        nums[0] += 1
        return nums

    j = 0
    # find up to what digit the num has 9s
    while j <= len(nums) - 1 and nums[j] == 9:
        nums[j] = 0
        j += 1

    if j <= len(nums) - 1:
        nums[j] += 1
        return nums
    else:
        # increasing precision
        nums.append(1)
        return nums


def main():
    num = 1999
    arr = convert_int_to_arr(num)
    op_arr = increment(copy.deepcopy(arr))
    op_num = convert_arr_to_int(op_arr)

    print("input number is {}, and its array is {}, output array is {} and its number is {}".
          format(num, arr, op_arr, op_num))


if __name__ == '__main__':
    main()
