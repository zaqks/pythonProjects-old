from itertools import permutations



nums = [4, 2, 1, 6, 7, 2]


def mlt_probs(state, n):
    perm = list(permutations(state, n))
    ln = len(perm)
    mlt_perm = []

    z = 1
    b = 0

    for i in range(ln):
        for i in range(3):
            z *= perm[b][i]
        b += 1
        mlt_perm.append(z)
        z = 1

    print(perm)
    print(mlt_perm)