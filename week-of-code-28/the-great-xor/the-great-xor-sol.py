#!/bin/python
import sys

q = int(raw_input().strip())
for a0 in xrange(q):
    x = long(raw_input().strip())
    count = 0
    for i in xrange(0,x):
        temp = 2**i
        if temp > x:
            print(temp - x - 1)
            break
        elif (temp == x):
            print(x-1)
            break