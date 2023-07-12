def nut(n):
    add = 2
    tot = 1
    for i in range(0,n-1):
        for i in range(0,add):
            tot = str(tot) + str(add)
        add += 1
    return(int(tot))

print(nut(100))