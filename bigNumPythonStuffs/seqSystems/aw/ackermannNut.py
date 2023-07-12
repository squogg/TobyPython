def nut(n):
    add = 2
    tot = 1
    for i in range(0,n-1):
        for i in range(0,add):
            tot = str(tot) + str(add)
        add += 1
    return(int(tot))

worm = [0,nut(69420)]
rowNum = 1
n = 0

while worm != []:
    lastTerm = worm[-1]
    if lastTerm == 0:
        worm.pop(-1)
        rowNum += 1
    else:
        worm.pop(-1)
        for i in range(0,rowNum):
            worm.append(lastTerm-1)
            rowNum += 1
    n += 1
print(n)