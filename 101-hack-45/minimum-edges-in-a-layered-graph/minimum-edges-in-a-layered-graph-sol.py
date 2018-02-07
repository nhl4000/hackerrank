#!/bin/python

import sys

def edges(layers, k):
    nodes = layers[k] # look at layer k
    toNodes = layers[k+1] # look at layer k+1
    return nodes * toNodes
    

n, k = raw_input().strip().split(' ')
n, k = [int(n),int(k)]
#n,k = [5,4]
#print([n,k])
            
layers = []
for layer in xrange(k):
    layers.append(1)

#layer[0] fixed at 1
#layer[k-1] fixed at 1

#print(layers)
if k > n:
    print("-1")
else:
    if sum(layers) != n:
        layers[k-2] += n-sum(layers)
    #print layers

    s = 0
    for l in xrange(k-1):
        s += edges(layers, l)

    if k == 2 and n > 2:
        print("-1")
    else:
        print(s)
