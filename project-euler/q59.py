# constraints: 80 <= n <= 1500

n = 82
line = "32 66 50 20 11 0 42 66 33 19 13 20 47 66 37 14 58 67 43 23 14 17 49 67 46 20 6 51 66 55 9 39 67 45 3 25 56 66 39 14 37 34 65 51 22 8 1 40 65 32 17 14 21 45 65 36 12 57 66 41 20 15 19 50 66 44 23 7 49 65 54 11 36 66 47 0 24 58 65 38 12 38"

#print(ord('A'), ord('Z'), ord('a'), ord('z'), ord('0'), ord('9'))
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789();:,.'?-! "
valid_characters = []
for character in string:
    valid_characters.append(ord(character))

#print(valid_characters)

encoded_characters = list(map(int, line.split(' ')))

for a in range(97,123):
    for b in range(97,123):
        for c in range(97,123):
            c0 = a
            c1 = b
            c2 = c
            f = 1
            for p in range(len(encoded_characters)):
                if p % 3 == 0:
                    temp = encoded_characters[p] ^ c0
                if p % 3 == 1:    
                    temp = encoded_characters[p] ^ c1
                if p % 3 == 2:    
                    temp = encoded_characters[p] ^ c2

                if temp not in valid_characters:
                    f = 0
                    break
            if f==1:
                print(chr(a),end="")
                print(chr(b),end="")
                print(chr(c))
