##https://www.hackerrank.com/contests/codeagon/challenges/ugly-or-beautiful
import sys

def uglyOrBeautiful(n,a):
    

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        n = int(raw_input().strip())
        a = map(int, raw_input().strip().split(' '))
        result = uglyOrBeautiful(n,a)
        print result

