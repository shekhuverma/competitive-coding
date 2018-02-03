#!/bin/python
import math
import sys

def counterGame(n):
    t=False
    # Complete this function
    while(n!=1.0):
        if (n and (not(n & (n - 1))) ):
            n/=2
        else:
            n-=int(math.pow(2,int(math.log(n,2))))
        t=not(t)
    if t:
        return "Louise"
    else:
        return "Richard"
            

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        result = counterGame(n)
        print result

