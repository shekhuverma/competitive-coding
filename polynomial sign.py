import numpy as np
n=raw_input().strip()
n=int(n)
count=0
ans=True
temp=True
lis=[int(x) for x in raw_input().split()]
for a in xrange(0,n):
    if lis[a]!=0:
        ans=False
    else:
        ans=True
        break
if ans:
    print 0,0
else:
    for a in xrange(n,0,-1):
        if lis[a]!=0:
            if lis[a]<0:
                temp=False
                break
    if temp:
        print 1,
        if a and i:
            print -1,
        else:
            print 1,
    else:
        print -1,
        if a and i:
            print 1,
        else:
            print -1,
