
priority = 0

while True:
    try:
        s = input()
        t = input()
        u = input()

        a, b, c = set([*s]), set([*t]), set([*u])

        d = a.intersection(b.intersection(c)).pop()

        if d.isupper():
            priority += ord(d) - ord('A') + 27
        else:
            priority += ord(d) - ord('a') + 1

    except EOFError:
        break

print(priority)
