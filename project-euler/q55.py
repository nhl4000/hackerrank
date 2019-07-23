# constraints: 100 <= n <= 100,000
n = 100000
palindromes = {}

def isPalindrome(i):
    return str(i)[::-1] == str(i)

for i in range(1, n + 1):
    if (isPalindrome(i)):
        if i in palindromes:
            palindromes[i].append(i)
        else:
            palindromes[i] = [i]
    else:
        first_i = i
        for iteration in range(1, 60):
            i = int(str(i)[::-1]) + i
            if (isPalindrome(i)):
                if i in palindromes:
                    palindromes[i].append(first_i)
                else:
                    palindromes[i] = [first_i]
                break
                
largestVal = -1
largestKey = -1
for key, val in palindromes.items():
    if len(val) >= largestVal:
        largestVal = len(val)
        largestKey = key

print("%d %d" % (largestKey, largestVal))
