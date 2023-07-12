cage = [2]; row = 2; max = 5; n = 0

while cage:
    if cage[-1] == 0: cage.pop()
    else:
        if len(cage) < max: x = cage[-1]-1; cage.pop(); cage.append(x); cage.append(row)
        else:
            x = cage[-1]-1; cage.pop(); cage.append(x); row += 1
    n += 1
    print(cage)

print(n)