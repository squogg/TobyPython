worm = [64]
rowNum = 64
n = 0
iterations = 64

for i in range(0,iterations+1):
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
    worm = [n]
    rowNum = n
print(n)