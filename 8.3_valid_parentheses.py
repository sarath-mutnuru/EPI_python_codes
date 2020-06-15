def is_valid(exp):
    brackets = {')': '(', ']': '[', '}': '{'}
    st = []
    for c in exp:
        if c in brackets.values():
           st.append(c)
        if c in brackets:
            if not st or st.pop() != brackets[c]:
                return False
    return not st


def main():
    exp = 'a(}'
    print(is_valid(exp))


if __name__ == '__main__':
    main()
