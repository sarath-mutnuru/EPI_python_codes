def is_palindrome(s):
    """ test is input str s is palindrome after removing non-alphanuermic chars """

    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum() and s[left] != ' ':
            left += 1

        while left < right and not s[right].isalnum() and s[right] != ' ':
            right -= 1

        if s[right].lower() != s[left].lower():
            return False
        else:
            left += 1
            right -= 1

    return True


def main():
    s = "Able was I, ere I saw Elba"

    print("s is{}a palindrome".format(" " if is_palindrome(s) else " not "))


if __name__ == '__main__':
    main()
