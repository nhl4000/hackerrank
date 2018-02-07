#!/bin/python

import sys

c = 0

def d(a,b):
    return min(abs(a-b),c-abs(a-b))

def d_pairs(a,b):
    return min(d(a[0],b[0]), d(a[0],a[1]),d(a[0],b[1]),d(a[1],b[1]),d(b[0],a[1]),d(b[0],b[1]))

n,c = raw_input().strip().split(' ')
n,c = [int(n),int(c)]
for a0 in xrange(n):
    points = []
    for points_i in xrange(n):
        points_temp = map(int,raw_input().strip().split(' '))
        points.append(points_temp)
        
    
    #print(points)
    maxC = 0
    maxT = 0
    for a in points:
        for b in points:
            if a == c: continue
            #print([a,b])
            maxT = d_pairs(a,b)
            if maxC < maxT:
                maxC = maxT
    
    print(maxC)
    break    
