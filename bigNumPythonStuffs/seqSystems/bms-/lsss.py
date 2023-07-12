# initialise the sequence and counter, n should = f_ψ(ψ_Ι(ω,0)(0))(n) by the end
seq = [0,3,1,2,1,2,0,0,0]
row = 3
n = 0

for i in range(0,1): #c hange to while seq:
    # remove all trailing 0s
    seqLength = len(seq)-1
    if seq[len(seq)-1] == 0:
        while seq[len(seq)-1] == 0:
            seq.pop()
    print(seq) # delete

    # find bad root
    lastTerm = seq[-1]
    n = -2
    badRoot = -999
    while badRoot == -999:
        if seq[n] < lastTerm:
            badRoot = seq[n]
        else:
            n = n - 1
    print(badRoot) # delete

    # find ancestors
    check = badRoot
    if seq.index(badRoot) > 0:
        x = seq.index(badRoot)-1
    else:
        x = seq.index(badRoot)
    ancestors = []
    ancestors.append(badRoot)
    if x != 0:
        while x != 0:
            if seq[x] <= check:
                ancestors.append(seq[x])
                seq[x] = check
            else:
                x -= 1
    if ancestors[0] != 0:
        ancestors.append(0)
    ancestors.reverse()
    print(ancestors)