score = 0

points = {
    'YA': 4,
    'YB': 5,
    'YC': 6,
    'XA': 3,
    'XB': 1,
    'XC': 2,
    'ZA': 8,
    'ZB': 9,
    'ZC': 7
}

while True:
    try:
        s = input()
        score += points.get(f"{s[2]}{s[0]}")
    except EOFError:
        break

print(score)
