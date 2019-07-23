# constraints: 8 <= n <= 10000

n = 10000

def iterFunction(a, b):
    return a + b + b, a + b

a = 1
b = 1
for iteration in range(1, n + 1):
    [a, b] = iterFunction(a, b)
    if (len(str(a)) != len(str(b))):
        print(iteration)