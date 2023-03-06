from numpy import sort
from fmain2maths import *
from permutations import *

win_combs_gen(3)

player_state = [3, 5, 9, 1]

mlt_probs(player_state, 3)

for i in range(len(State.mlt_perm)):
    if State.mlt_perm[i] in Ref.mlt_combs:

        print(State.mlt_perm[i])
        cm = State.perm__mlt_perm[State.mlt_perm[i]]
        print(list(sort(cm)))

        if list(sort(cm)) in Ref.combs:
            print("yoo")
            break

