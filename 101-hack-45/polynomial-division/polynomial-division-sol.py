#!/bin/python

import sys
n=0
a=0
b=0
q=0

def normalize(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    if poly == []:
        poly.append(0)


def poly_divmod(num, den):
    #Create normalized copies of the args
    num = num[:]
    normalize(num)
    den = den[:]
    normalize(den)

    if len(num) >= len(den):
        #Shift den towards right so it's the same degree as num
        shiftlen = len(num) - len(den)
        den = [0] * shiftlen + den
    else:
        return [0], num

    quot = []
    divisor = float(den[-1])
    for i in xrange(shiftlen + 1):
        #Get the next coefficient of the quotient.
        mult = num[-1] / divisor
        quot = [mult] + quot

        #Subtract mult * den from num, but don't bother if mult == 0
        #Note that when i==0, mult!=0; so quot is automatically normalized.
        if mult != 0:
            d = [mult * u for u in den]
            num = [u - v for u, v in zip(num, d)]

        num.pop()
        den.pop(0)

    normalize(num)
    return quot, num

def poly(l,r,c):
    p = []
    for i in xrange(l,r+1):
        p.append(c[i] % 1000000007)
    return p


n,a,b,q = raw_input().strip().split(' ')
n,a,b,q = [int(n),int(a),int(b),int(q)]
qofx = [b,a]
c = map(int, raw_input().strip().split(' '))
for a0 in xrange(q):
    queryType,first,second = raw_input().strip().split(' ')
    queryType,first,second = [int(queryType),int(first),int(second)]
    if queryType == 1:
        # Replace ci with x
        c[first] = second
    else:
        p = poly(first, second, c)
        q, r = poly_divmod(p, qofx)
        #print(q,r)
        f = 0
        for z in q:
            if not z.is_integer():
                f = 1
        if (f == 0) or (r[0] == 0):
            print "Yes"
        else:
            print "No"