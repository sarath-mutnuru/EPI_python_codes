def is_duplicate(arr):
    arr = list(filter(lambda x: x != 0, arr))
    return len(arr) != len(list(set(arr)))


def is_valid_board(board):
    vals =[]
    for i in range(9):
        vals.append(is_duplicate([board[i][j] for j in range(9)]))
        vals.append(is_duplicate([board[j][i] for j in range(9)]))
    for I in range(0, 9, 3):
        for J in range(0, 9, 3):
            region = [board[i][j] for i in range(I, I + 3) for j in range(J, J + 3)]
            vals.append(is_duplicate(region))
    return not any(vals)


def main():
    board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 0, 0, 0, 1],
             [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0],
             [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    is_valid = is_valid_board(board)
    if is_valid:
        print("the board is valid")
    else:
        print("the board is not valid")


if __name__ == '__main__':
    main()