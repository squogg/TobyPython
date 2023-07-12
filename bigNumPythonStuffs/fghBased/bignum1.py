# attempt at making a large number

n = 3
def f0(n):
    n += 1
    return(n)

def f1(n):
    for i in range(0,n):
        n = int(f0(n))
    return(n)

def f2(n):
    for i in range(0,n):
        n = int(f1(n))
    return(n)

def f3(n):
    for i in range(0,n):
        n = int(f2(n))
    return(n)

print(f3(f3(f3(n)))) # f_4(3)