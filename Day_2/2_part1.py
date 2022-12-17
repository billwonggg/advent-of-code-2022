score = 0

points = {
    'YA': 8,
    'YB': 5,
    'YC': 2,
    'XA': 4,
    'XB': 1,
    'XC': 7,
    'ZA': 3,
    'ZB': 9,
    'ZC': 6
}

while True:
    try:
        s = input()
        score += points.get(f"{s[2]}{s[0]}")
    except EOFError:
        break

print(score)
