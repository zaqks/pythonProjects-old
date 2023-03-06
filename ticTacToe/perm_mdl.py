from itertools import permutations

class State:
    perm = []
    mlt_perm = []
    perm__mlt_perm = {}

def mlt_probs(state, n):
    State.perm = list(permutations(state, n))
    ln = len(State.perm)
    State.mlt_perm = []

    z = 1
    b = 0

    for i in range(ln):
        for i in range(n):
            z *= State.perm[b][i]
        b += 1
        State.mlt_perm.append(z)
        z = 1

    for i in range(ln):
        State.perm__mlt_perm[State.mlt_perm[i]] = State.perm[i]

    print(State.perm)
    print(State.mlt_perm)
    print(State.perm__mlt_perm)
