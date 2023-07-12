# Prerequisites 
seq = [0,3]
rowNum = 3
# num here is the final output
num = 0

for i in range(0,5):
    # Remove trailing 0s
    seqLength = len(seq)-1
    if seq[len(seq)-1] == 0:
        while seq[len(seq)-1] == 0:
            seq.pop()

    # Find bad root and delta
    lastTerm = seq[-1]; n = -2; badRoot = -999
    while badRoot == -999:
        if seq[n] < lastTerm:
            badRoot = seq[n]
        else:
            n -= 1
    delta = lastTerm - badRoot - 1

    # Find and copy bad part
    badPart = []
    seqLength = len(seq)-1
    if badRoot == 0: lol = seq[badRoot]
    else: lol = seq[len(seq[0:badRoot])-1]
    seq.pop()
    for i in range(lol,seqLength):
        badPart.append(seq[lol]); lol += 1
    bpLength = len(badPart)

    # Expand
    mult = 1
    for i in range(0,rowNum):
        lol = 0
        for i in range(0,bpLength):
            seq.append(badPart[lol] + (mult * delta)); lol += 1
        mult += 1
    rowNum += 1; num += 1; print(seq, rowNum)
print(num)