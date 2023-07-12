def hyper(a,b,c):
    if c == 1:
        result = a+b
    else:
        result = a
        for i in range(0,b-1):
            result = int(hyper(result,a,c-1))
    return(result)

def hf(a,b):
    diff = a-1
    for i in range(1,a):
        a = int(hyper(a,diff,b+2))
        diff -= 1
    return(a)

print(hf(3,1))