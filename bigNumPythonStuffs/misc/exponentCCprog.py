a = 10; b = 10; n = 0; x = 0

while n < 2**32:
    while a != 0: a -= 1; b += 1; x += 1
    if a == 0:
        n += 1
        while a < b: a += 1; x += 1

print(x)