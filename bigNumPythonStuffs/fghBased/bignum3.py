# attempt at making f_omega2(n)

def f(a,n): #f_a<omega(n)
    if a == 0:
        n += 1
        return(n)
    else:
        for i in range(0,n):
            n = int(f(a-1,n))
    return(n)

def g(a,n):
    if n == 0: # acts as f_omega(n)
        a = n
        n = int(f(a,n))
    elif n == 1: # acts as f_omega+1(n)
        for i in range(0,n):
            a = n
            n = int(f(a,n))
    else: # acts as f_omega+n(n) = f_omega2(n)
        for i in range(0,n):
            a = n
            n = int(g(a-1,n))
    return(n)

print(g(g(g(g(g(99,99),99),99),99),99)) # f_f_f_f_f_omega2(99)(99)(99)(99)(99) lmao