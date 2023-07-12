# Prerequisites 
seq = []
baseLength = int(input("Seq length = "))
for i in range(0,baseLength):
    term = int(input("Term = ")); seq.append(term)
    if seq[0] != 0:
        print("Invalid term, try again"); seq.pop(); baseLength += 1
    if len(seq) > 1:
        if seq[-1] > seq[-2] + 1:
            print("Invalid term, try again"); seq.pop(); baseLength += 1
rowNum = int(input("Row number = "))
# num here is the final output
num = 0

while seq != []:
    # Remove trailing 0s
    seqLength = len(seq)-1
    if seq[len(seq)-1] == 0:
        while seq[len(seq)-1] == 0: seq.pop()

    # Find bad root
    lastTerm = seq[-1]; n = -2; badRoot = -999
    while badRoot == -999:
        if seq[n] < lastTerm: badRoot = seq[n]
        else: n -= 1

    # Find and copy bad part
    badPart = []; seqLength = len(seq)-1; lol = seq[badRoot]; seq.pop()
    for i in range(lol,seqLength):
        badPart.append(seq[lol]); lol += 1
    bpLength = len(badPart)

    # Expand
    for i in range(0,rowNum):
        lol = 0
        for i in range(0,bpLength):
            seq.append(badPart[lol]); lol += 1
    rowNum += 1; num += 1
print(num)