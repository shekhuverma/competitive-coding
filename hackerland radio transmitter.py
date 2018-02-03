import sys
n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
x = map(int,raw_input().strip().split(' '))
ans=0
i=0
x=sorted(x)
while(i<n):
    ans+=1
    loc=x[i]+k
    while(i<n and x[i]<=loc):
        i+=1
    i-=1
    loc=x[i]+k
    while(i<n and x[i]<=loc):
        i+=1
print ans
