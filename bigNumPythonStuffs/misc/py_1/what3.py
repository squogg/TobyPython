def L(x):
 if x<5:return 9
 n=L(x-1)+1
 while 1:
  d=range(2**n)
  l=[[None]*len(d)for i in d]
  while any(None in i for i in l):
   for x in d:
    l[x][0]=(x+1)%2**n
    for y in d:
     for z in d:
      try:l[x][l[y][z]]=l[l[x][y]][l[x][z]]
      except:1
  r=2**x
  if l[0][:r]==l[0][r:2*r]:return n
  n+=1
x=L(9)
