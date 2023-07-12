def k(a,b,c): # this = a{c}b
    if c < 1:
        print("enter a number >= 1")
    elif c == 1:
        return(a**b)
    else:
        d = a
        for i in range(0,b-1):
            a = int(k(d,a,c-1))
        return(a)

def g(n):
    if n == 0:
        return(4)
    else:
        for i in range(0,n):
            n = k(3,3,int(g(n-1)))
        return(n)

print(g(64))