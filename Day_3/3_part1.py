
priority = 0

while True:
    try:
        s = input()
        a, b = set([*s[:len(s)//2]]), set([*s[len(s)//2:]])

        c = a.intersection(b).pop()

        if c.isupper():
            priority += ord(c) - ord('A') + 27
        else:
            priority += ord(c) - ord('a') + 1

    except EOFError:
        break

print(priority)
