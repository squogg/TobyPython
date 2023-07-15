*S,x=0,9,9
P=lambda A,i,j:[k for k in range(i)if A[k]<A[j]]
while S:
 x*=x;k,*m=0,len(S)-1
 while P(S,m[k],-1):m+=[max(P(S,m[k],-1))];k+=1
 if k<1:continue
 N=[m[i+1]-m[i]for i in range(m[0])]
 if N[0]-1:
  f=P(N,k,0);r=min(f) if f else 0
  d=S[-1]-S[r]-1
 else:d=0;r=m[1]
 S.pop()
 exec("S+=[a+d for a in S[r-m[0]:]];"*x)
