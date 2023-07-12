worm = [999]; rowNum = 999; n = 0

while worm != []:
    lastTerm = worm[-1]
    if lastTerm == 0:
        worm.pop(-1)
        rowNum += rowNum
    else:
        worm.pop(-1)
        for i in range(0,rowNum):
            worm.append(lastTerm-1)
            rowNum **= rowNum
    n += 1
print(n)