# initialise the pair sequence (0,0)(1,1)(2,1)(3,1)[3]
seq = [[0,0],[1,1],[2,1],[3,1]] 
display = [[0,0],[1,1],[2,1],[3,1]]
rowNum = 3

steps = 0

while seq != []:

    #remove trailing 0s
    if seq[-1][0] and seq[-1][1] == 0:
        while seq[-1][0] and seq[-1][1] == 0:
            seq.pop(-1)

    # find bad root + ancestors of both sequences
    ancestors1 = []
    ancestors2 = []
    n = len(seq)-2
    while n > -1:
        if seq[n][0] < seq[n+1][0]:
            ancestors1.append(seq[n][0])
        else:
            ancestors1.append(-1)
        n -= 1
    n = len(seq)-2
    while n > -1:
        if seq[n][1] < seq[n+1][1]:
            ancestors2.append(seq[n][1])
        else:
            ancestors2.append(-1)
        n -= 1
    ancestors1.reverse()
    ancestors2.reverse()
    n = -1
    badRoot1 = -1
    badRoot2 = -1
    while badRoot1 == -1 and badRoot2 == -1:
        if ancestors1[n] == ancestors2[n] and ancestors1[n] != -1:
            badRoot1 = ancestors1[n]
            badRoot2 = ancestors2[n]
        else:
            n -= 1

    # construct bad part of each sequence
    badPart1 = []
    badPart2 = []
    n = 0
    for i in range(0,len(seq)-1):
        badPart1.append(seq[n][0])
        badPart2.append(seq[n][1])
        n += 1

    # calculate delta
    delta = seq[-1][0] - badRoot1
    mult = 1

    #  expand
    n = 0
    seq.pop(-1)
    for i in range(0,rowNum):
        for  i in range(0,len(badPart2)):
            seq.append([badPart1[n]+delta*mult,badPart2[n]])
            n += 1
        n = 0
        mult += 1
    steps += 1
    print(steps)

print(display,"[",rowNum,"] = ",steps)