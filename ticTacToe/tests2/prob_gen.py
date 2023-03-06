from itertools import permutations
from math import factorial

n = 2
nums = [1, 2, 3, 4, 6, 7, 8, 9]
chn = factorial(2)

perm = factorial(n*n)

def twfk(n):
    return factorial(n*n)/(factorial(n*n-n))




print(list(permutations(nums, 4)))