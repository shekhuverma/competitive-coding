##https://www.hackerrank.com/challenges/sherlock-and-squares/problem
import math
t=input()
for a in xrange(t):
    x,y=[int(x) for x in raw_input().strip().split()]
    print int(math.floor(math.sqrt(y))-math.ceil(math.sqrt(x))+1)
        
