#!/bin/python

import sys


n,c,m = raw_input().strip().split(' ')
n,c,m = [int(n),int(c),int(m)]
p = map(int, raw_input().strip().split(' '))

if (c*m >= max(p)) and (n > max(p)):
    print "Yes"
elif (c*m < max(p)):
    print "No"
else:
    print "Yes"