#!/usr/bin/py
# Head ends here
def pairs(a,k,n):
    ans=0
    #a contains array of numbers and k is the value of difference
    a.sort()
    l=1
    i=0
    while(l<n):
        diff=a[l]-a[i]
        if diff==k:
            ans+=1
            i+=1
        elif diff>k:
            i+=1
        elif diff<k:
            l+=1
    return ans
# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k,_a_size)
