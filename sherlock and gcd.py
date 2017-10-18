#https://www.hackerrank.com/challenges/sherlock-and-gcd/problem
def gcd(a, b):
        if b==0:
            return a
        else:
            return gcd(b, a%b)
t=input()
for a in range(t):
    n=input()
    lis=[int(x) for x in raw_input().strip().split()]
    no=lis[0]
    for i in range(1,n):
        no=gcd(no,lis[i])
    if no<=1:
        print "YES"
    else:
        print "NO"
    
