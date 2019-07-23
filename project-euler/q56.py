# constraints: 5 <= n <= 200
n = 200

summer_values = []

for a in range(1, n):
    for b in range(1, n):
        num = pow(a,b)
        summer = 0
        while num > 0:
            d = num%10
            num = num//10
            summer += d
        #print(summer)
        summer_values.append(summer)


print(max(summer_values))
