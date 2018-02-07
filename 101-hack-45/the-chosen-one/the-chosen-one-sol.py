#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

maxDivisor = max(a)
targetCount = n - 1

for d in xrange(2, maxDivisor+1):
    count = 0
    ncount = 0
    for e in a:
        if (e % d == 0):
            #print([e,d])
            count += 1
        else:
            ncount += 1
        
        if ncount == 2:
            break            
    if count == targetCount:
        print(d)
        break
    else:
        count = 0