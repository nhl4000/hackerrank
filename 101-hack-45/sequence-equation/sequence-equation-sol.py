#!/bin/python

import sys
n = int(raw_input().strip())
p = map(int,raw_input().strip().split(' '))

for x in xrange(1,n+1):
    #print("Find x = %d" % x)
    p1 = 0
    pos = 1
    for y in p:
        #print([y,x])
        if y == x:
            p1 = pos
            break
        pos +=1
    #print(p1)
    y = 0
    pos2 = 1
    for a in p:
        if a == p1:
            y = pos2
            break
        pos2 +=1
    print(y)
    #print(p[i-1])
            