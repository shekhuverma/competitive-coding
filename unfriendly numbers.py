import math
# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    b = map(int, raw_input().strip().split(" "))
    n=a[0]
    f=a[1]
    answer = 0
    lis=set([])
    lis2=set([])
    i = 1
    ans=0
    while i <= math.sqrt(f) + 1 : 
        if (f % i == 0) :    
            # If divisors are equal, print only one
            if (f / i == i) :
                lis.add(i)
            else :
                # Otherwise print both
                lis.add(i)
                lis.add(n/i)
        i = i + 1
    i=1
    for a in b:
        while i <= math.sqrt(a) + 1 :
            if (a% i == 0) :
            # If divisors are equal, print only one
                if (a/ i == i) :
                    lis2.add(i)
                else :
                    lis2.add(i)
                    lis2.add(n/i)
            i = i + 1
            lis2.add(a)
    print lis
    print b
    print lis2
    print len(lis.difference(lis2))
