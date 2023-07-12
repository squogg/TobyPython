def k(a,b,c): # this = a{c}b
    if c < 1: print("enter a number >= 1")
    elif c == 1:return(a**b)
    else:
        d = a
        for i in range(0,b-1): a = int(k(d,a,c-1))
        return(a)

def fac(n):
    diff = n-1
    for i in range(1,n):
        n *= diff; diff -= 1
    return(n)

def hf(a,b):
    if b == 0: return(int(fac(a)))
    else:
        n = 4; res = int(k(3,2,b))
        for i in range(0,b-3):
            res = int(k(n,res,b)); n += 1
        return(res)

print(hf(3,int(hf(33,int(hf(3,3))))))