#!/bin/python

import sys
from itertools import chain, combinations
sys.setrecursionlimit(100000)

def powerset(iterable):
    xs = list(iterable)
    return chain.from_iterable( combinations(xs,n) for n in xrange(len(xs)+1) )

def list_powerset(lst):
    result = [[]]
    for x in lst:
        result.extend([subset + [int(x)] for subset in result])
    return result

def list_powerset2(lst):
    return reduce(lambda result, x: result + [subset + [int(x)] for subset in result],
                  lst, [[]])

n = int(raw_input().strip())
number = raw_input().strip()
count = 0
#seta = powerset(number)
for s in powerset(number):
    if len(s) == 0: continue
    a = ""
    for i in s:
        a += str(i)
    if (long(a) == 0):
        count += 1
    elif (long(a) % 8 == 0):
        count += 1

    if (count == ((10 ** 9) + 7)):
        count = 0

print(count)