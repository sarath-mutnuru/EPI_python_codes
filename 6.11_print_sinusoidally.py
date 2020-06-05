def get_sinusoidally(s):
    ans = []
    for i in range(1, len(s), 4):
        ans.append(s[i])
    for i in range(0, len(s), 2):
        ans.append(s[i])
    for i in range(3, len(s), 4):
        ans.append(s[i])
    return ''.join(ans)

def main():
    s = 'Hello_world'
    ans = get_sinusoidally(s)
    print("string is {}, sinusoid format is {}".format(s, ans))


if __name__ == '__main__':
    main()
