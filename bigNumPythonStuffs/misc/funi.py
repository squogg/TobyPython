def a(x,y,z):
    if x == 0:
        return y**z
    elif y == 0:
        return int(a(x-1,y,z+x))
    elif z == 0:
        return int(a(x**x,y-1,z))
    else:
        return int(a(int(a(x,y,0)),int(a(x,y,0)),z-1))

print(a(10,10,10))