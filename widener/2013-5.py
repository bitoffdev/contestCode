from itertools import *
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

stocks = map(int, raw_input().split("-")[0].split())
possible = []
solutions = []
greatest = 0
for subset in powerset(stocks):
    subset = list(subset)
    subset = [i for i in subset if isinstance(i, int)]
    if all(subset[i]>subset[i+1] for i in range(0, len(subset)-1)):
        possible.append(subset)
        if len(subset) > greatest:
            greatest = len(subset)
for item in possible:
    if len(item)==greatest and item not in solutions:
        solutions.append(item)
print len(solutions)
for item in solutions:
    print " ".join(map(str,item))

