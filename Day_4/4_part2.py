not_overlap = 0
total = 0

while True:
    try:
        s = input()
        total += 1
        a, b = s.split(',')
        aRange, bRange = list(map(int, a.split('-'))), \
            list(map(int, b.split('-')))
        if (aRange[1] < bRange[0]) or (bRange[1] < aRange[0]):
            not_overlap += 1
    except EOFError:
        break

print(total - not_overlap)
