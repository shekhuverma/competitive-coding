import math
from fractions import gcd
lis=[]
def printDivisors(n) :
    lis=set([])
    i = 1
    while i <= math.sqrt(n) + 1 : 
        if (n % i == 0) :
            lis.add(i)
            lis.add(n/i)
        i = i + 1
    return lis
com=[int(x) for x in raw_input().split()]
for a in xrange(com[1],com[2]+1):
    lis.extend(printDivisors(a))
for _ in range(com[0]):
    n=input()
    count=0
    for a in lis:
        if a%n!=0:
            count+=1
    print count
