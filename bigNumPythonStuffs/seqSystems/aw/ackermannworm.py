worm = [1,3]; rowNum = 3; n = 0

while worm != []:
    lastTerm = worm[-1]
    if lastTerm == 0:
        worm.pop(-1); rowNum += 1
    else:
        worm.pop(-1)
        for i in range(0,rowNum):
            worm.append(lastTerm-1); rowNum += 1
    n += 1
print(n)