count = 0

while True:
    try:
        s = input()
        a, b = s.split(',')
        aRange, bRange = list(map(int, a.split('-'))), \
            list(map(int, b.split('-')))
        if (aRange[0] >= bRange[0] and aRange[1] <= bRange[1]) \
                or (bRange[0] >= aRange[0] and bRange[1] <= aRange[1]):
            count += 1
    except EOFError:
        break

print(count)
