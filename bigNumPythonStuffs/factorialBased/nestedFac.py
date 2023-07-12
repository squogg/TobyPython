def nestFac(a,b):
    for i in range(0,b):
        diff = a-1
        for i in range(1,a):
            a *= diff
            diff -= 1
        a = a
    return(a)

print(nestFac(999,999))