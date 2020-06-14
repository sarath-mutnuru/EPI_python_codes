def eval_terms(num1, num2, op):
    num1, num2 = int(num1), int(num2)
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2
    if op == '*':
        return num1 * num2
    return num1//num2 if num1*num2 >= 0 else -1 * (-1*num1//num2)


def eval_rpn(expr):
    arr = expr.split(",")
    res = []
    for i in range(len(arr)):
        if arr[i] in ['+', '-', '*','/']:
            b = res.pop()
            a = res.pop()
            res.append(str(eval_terms(a, b, arr[i])))
        else:
            res.append(arr[i])
    return res.pop()


def main():
    # expr = '3,4,+,2,*,1,+'
    # expr = '5,2,/'
    expr = '4,13,5,/,+'
    ans = eval_rpn(expr)
    print(ans)


if __name__ == '__main__':
    main()