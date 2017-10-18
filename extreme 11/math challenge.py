import math
def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo,mid) * range_prod(mid+1,hi)
    if lo == hi:
        return lo
    return lo*hi

def factorial(n):
    if n < 2:
        return 1
    return range_prod(1,n)
t=input()
for _ in xrange(t):
    com=[int(x) for x in raw_input().split()]
    ans=factorial(com[1])/factorial(com[2])*factorial(com[0]-com[1])
    print (com[0]**ans)%10**9+7
