# big number 4
def f(a,n):
    if a == 0:
        n **= n
        return(n)
    else:
        for i in range(0,n**n):
            n = int(f(a-1,n))
    return(n)

def g(a,n):
    if n == 0:
        a = n
        n = int(f(a,n))
    elif n == 1:
        for i in range(0,n**n):
            a = n
            n = int(f(a,n))
    else:
        for i in range(0,n**n):
            a = n
            n = int(g(a-1,n))
    return(n)

def h(a,n):
    if n == 0:
        n = int(g(a,a))
    elif n == 1:
        for i in range(0,int(g(a,a))):
            a = n
            n = int(g(a,n))
    else:
        for i in range(0,g(a,n)):
            a = n
            n = int(h(a-1,n))
    return(n)

print(h(999,999))