#!/bin/python

import sys
import random


def getProb(b):
    #print(b)
    n = len(b)
    count = 0
    indexes = set()
    for x in xrange(n):
        #print ([x,b[x], b[n-1-x]])
        if b[x] == 'W': # or b[n-1-x] == 'W': 
            count += 1    
            indexes.add(x)
        elif b[n-1-x] == 'W':
            count +=1
            indexes.add(n-1-x)
    #print("%s has prob %f" % (b, float(count)/float(n)))
    return [indexes, float(count)/float(n)]

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
balls = raw_input().strip() 

expected = 0
count = 0
options = set()
options.add(balls)
opt2 = set()
for i in xrange(1,k+1):
    #for x in xrange(1,len(balls)-i+1): # = int(random.uniform(1,len(balls)-i+1))
    level_prob = 0
    level_size = len(options)
    for b in options:
        idxs, prob = getProb(b)
        opt2 = set()
        #print(["idxs",idxs])  
        for c in idxs:
            #print("in indxs : %d" % len(b))
            if len(b) == 2:
                opt2.add(b[1-c])
            else:
                opt2.add(b[:c] + b[(c+1):])
        #print(["next k has to check:", options])
        
        level_prob += float(1)/float(level_size) * float(prob)
        #print([i, float(1)/float(level_size) * float(prob)])  
        #print(level_prob)
    #print(balls)
    options = opt2
    expected += level_prob

print("%.10f" % expected)