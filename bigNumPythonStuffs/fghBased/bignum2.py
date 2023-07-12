# attempt at making f_omega+1(n)

def f(a,n): #f_a->omega(n)
    if a == 0:
        n += 1
        return(n)
    else:
        for i in range(0,n):
            n = int(f(a-1,n))
    return(n)

def g(n):
    for i in range(0,n):
        a = n
        n = int(f(a,n))
    return(n)

print(g(g(g(g(g(64)))))) # f^5_omega+1(64)