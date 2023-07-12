def A(x,y):
    if x == 0:
        return(x+1)
    elif y == 0:
        n = int(A(x-1,1))
        return(n)
    else:
        n = int(A(x-1,int(A(x,y-1))))
        return(n)

print(A(4,3))