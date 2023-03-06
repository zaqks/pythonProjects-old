n = 3

def win_combs_gen(n):
    "3mar l grid"

    grid = []
    combs = []

    mlt_combs = []

    combs__mlt_combs = {}

    for i in range(n*n):
        grid.append(i+1)

    "3mar l comb bl mini"
    for i in range(n*2 + 2):
        combs.append([])

    "x fill"
    a = 0
    b = 0

    for i in range(n):
        for i in range(n):
            combs[b].append(grid[a])
            a += 1
        b += 1

    "y fill"

    for i in range(n):
        a = i

        for i in range(n):
            combs[b].append(grid[a])
            a += n
        b += 1

    "cross fill1"

    for i in range(1):
        a = i

        for i in range(n):
            combs[b].append(grid[a])
            a += (n+1)
        b += 1

    "cross fill2"
    for i in range(1):
        a = n-1

        for i in range(n):
            combs[b].append(grid[a])
            a += (n-1)
        b += 1


    "mlt combs calc"

    rslt = 1
    k = 0

    for i in range(n*2+2):
        for i in range(n):
            rslt *= combs[k][i]
        mlt_combs.append(rslt)
        rslt = 1
        k += 1


    "association"

    for i in range(n*2+2):
        combs__mlt_combs[mlt_combs[i]] = combs[i]


    print(combs)
    print(mlt_combs)
    print(combs__mlt_combs)

win_combs_gen(3)