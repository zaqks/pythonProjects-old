class Ref:
    combs = []
    mlt_combs = []
    combs__mlt_combs = {}


def win_combs_gen(n):
    "3mar l grid"

    grid = []


    for i in range(n*n):
        grid.append(i+1)

    "3mar l comb bl mini"
    for i in range(n*2 + 2):
        Ref.combs.append([])

    "x fill"
    a = 0
    b = 0

    for i in range(n):
        for i in range(n):
            Ref.combs[b].append(grid[a])
            a += 1
        b += 1

    "y fill"

    for i in range(n):
        a = i

        for i in range(n):
            Ref.combs[b].append(grid[a])
            a += n
        b += 1

    "cross fill1"

    for i in range(1):
        a = i

        for i in range(n):
            Ref.combs[b].append(grid[a])
            a += (n+1)
        b += 1

    "cross fill2"
    for i in range(1):
        a = n-1

        for i in range(n):
            Ref.combs[b].append(grid[a])
            a += (n-1)
        b += 1


    "mlt combs calc"

    rslt = 1
    k = 0

    for i in range(n*2+2):
        for i in range(n):
            rslt *= Ref.combs[k][i]
        Ref.mlt_combs.append(rslt)
        rslt = 1
        k += 1


    "association"

    for i in range(n*2+2):
        Ref.combs__mlt_combs[Ref.mlt_combs[i]] = Ref.combs[i]


    print(Ref.combs)
    print(Ref.mlt_combs)
    print(Ref.combs__mlt_combs)
