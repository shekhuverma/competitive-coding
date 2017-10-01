# sherlock and array :-https://www.hackerrank.com/challenges/sherlock-and-array
#logic

t=input()
i=0
while(i<t):
    n=input()
    lis=[int(x) for x in raw_input().split()]
    lis=lis[:n]
    ans=False
    s=[0]*(n+1)
    for a in range(1,n+1):
        s[a]=s[a-1]+lis[a-1]
    for b in range(1,n+1):
        if s[b-1]==s[n]-s[b]:
            ans=True
            break
    if(ans):
        print "YES"
    else:
        print "NO"
    i+=1

    
