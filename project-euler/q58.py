# constraints : 8 <= n <= 60
import math
import random
#import time

# Utility function to do 
# modular exponentiation. 
# It returns (x^y) % p 
def power(x, y, p): 
    # Initialize result 
    res = 1
    # Update x if it is more than or 
    # equal to p 
    x = x % p
    while (y > 0): 
        # If y is odd, multiply 
        # x with result 
        if (y & 1): 
            res = (res * x) % p
        # y must be even now 
        y = y>>1 # y = y/2 
        x = (x * x) % p
    return res
  
# This function is called 
# for all k trials. It returns 
# false if n is composite and  
# returns false if n is 
# probably prime. d is an odd  
# number such that d*2<sup>r</sup> = n-1 
# for some r >= 1 
def miillerTest(d, n): 
    # Pick a random number in [2..n-2] 
    # Corner cases make sure that n > 4 
    a = 2 + random.randint(1, n - 4)
    # Compute a^d % n 
    x = power(a, d, n)
    if (x == 1 or x == n - 1): 
        return True
    # Keep squaring x while one  
    # of the following doesn't  
    # happen 
    # (i) d does not reach n-1 
    # (ii) (x^2) % n is not 1 
    # (iii) (x^2) % n is not n-1 
    while (d != n - 1): 
        x = (x * x) % n
        d *= 2
  
        if (x == 1): 
            return False
        if (x == n - 1):
            return True
    # Return composite 
    return False
  
# It returns false if n is  
# composite and returns true if n 
# is probably prime. k is an  
# input parameter that determines 
# accuracy level. Higher value of  
# k indicates more accuracy. 
def isPrime(n, k): 
    # Corner cases 
    if (n <= 1 or n == 4): 
        return False
    if (n <= 3): 
        return True
    # Find r such that n =  
    # 2^d * r + 1 for some r >= 1 
    d = n - 1
    while (d % 2 == 0): 
        d //= 2
    # Iterate given nber of 'k' times 
    for i in range(k): 
        if (miillerTest(d, n) == False): 
            return False
    return True
 
# Driver Code 
# Number of iterations 
k = 4


def getRatio(diag):
    dem = len(diag)
    
    primes = []
    for i in diag:
        if (isPrime(i, k)):
            primes.append(i)
    num = len(primes)
    return int(math.ceil(float(float(num)/float(dem)*100.0)))

#diagonals = [1,3,5,7,13,17,31,37,43]
#n = 8

#diagonals = [1]
number_of_diag = 1
number_of_primes = 0
sides = 7
n = (sides/2) + 1 # 4
end = 1
bottom_right = 1
level = 1

target_goal = 8

for i in range(1, 6000000):
    number_of_diag += 4

    top_right = bottom_right + i + level
    top_left = top_right + i + level
    bottom_left = top_left + i + level
    bottom_right = bottom_left + i + level

    if (isPrime(top_right, k)):
        number_of_primes += 1
    if (isPrime(top_left, k)):
        number_of_primes += 1
    if (isPrime(bottom_left, k)):
        number_of_primes += 1
    if (isPrime(bottom_right, k)):
        number_of_primes += 1
    

    #end = bottom_right
    level += 1
    side_length = i + level
    #print(side_length, bottom_right, top_right, top_left, bottom_left)
    #time.sleep(1)
    #print(diagonals)
    if (side_length == 3): continue
    if (int(float(float(number_of_primes)/float(number_of_diag))*100) < target_goal):
        print(side_length)
        print(number_of_primes, number_of_diag, float(number_of_primes)/float(number_of_diag))
        break


#print(side_length)
#print(diagonals, len(diagonals), getRatio(diagonals))


