a = [[5, 9, 0, 2, 8, 1, 0, 0, 2], [0, 2, 4, 8, 1, 6, 9, 2, 0]]
for ridx, row in enumerate(a):
    for cidx, val in enumerate(row):
        if val == 0:
            a[ridx][cidx] = 'X'
