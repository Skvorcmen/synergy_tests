word = input()

glas = 0
sogl = 0
a = 0
e = 0
i = 0
o = 0
u = 0

for letter in word:
    if letter == "a":
        a += 1
        glas += 1
    elif letter == "e":
        e += 1
        glas += 1
    elif letter == "i":
        i += 1
        glas += 1
    elif letter == "o":
        o += 1
        glas += 1
    elif letter == "u":
        u += 1
        glas += 1
    else:
        sogl += 1

print(glas)
print(sogl)
print(a if a > 0 else False)
print(e if e > 0 else False)
print(i if i > 0 else False)
print(o if o > 0 else False)
print(u if u > 0 else False)
