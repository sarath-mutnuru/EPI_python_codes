def permute_array(arr, permute_order):
    """ permute_order will have destination positions of the elements in array """
    for i,_ in enumerate(arr):
        if permute_order[i] != -1:

            j = i
            temp1 = arr[j]
            while permute_order[j] != -1:
                temp2 = temp1
                temp1 = arr[permute_order[j]]
                arr[permute_order[j]] = temp2
                k = j
                j = permute_order[j]
                permute_order[k] = -1


def main():
    arr = 'a,b,c,d'.split(',')
    permute_order = [2, 0, 1, 3]
    permute_array(arr, permute_order)
    print(arr)


if __name__ == '__main__':
    main()