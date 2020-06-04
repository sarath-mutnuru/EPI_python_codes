MAP = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
EXCEPTION_LIST = [('I', 'V'), ('I', 'X'), ('X', 'L'), ('X', 'C'), ('C', 'D'), ('C', 'M')]


def roman_to_int(roman):
    if not len(roman):
        return 0
    if roman[0] not in MAP:
        raise ValueError("{} is not a valid Roman Numeral".format(roman[0]))
    ans = MAP[roman[0]]
    for i in range(1, len(roman)):
        if roman[i] not in MAP:
            raise ValueError("{} is not a valid Roman Numeral".format(roman[i]))
        if MAP[roman[i]] <= MAP[roman[i-1]]:
            ans += MAP[roman[i]]
        else:
            if (roman[i-1], roman[i]) not in EXCEPTION_LIST:
                raise ValueError("{}{} is not a valid sequence".format(roman[i-1], roman[i]))
            else:
                ans = ans + MAP[roman[i]] - 2*MAP[roman[i-1]]
    return ans


def main():
    roman = 'LVIII'
    print("Roman {} is int {} ".format(roman, roman_to_int(roman)))


if __name__ == '__main__':
    main()

