n = int(raw_input().strip())
A = map(int, raw_input().strip().split(' '))
s=[0]*(n+1)
count=0
for a in range(1,n+1):
    s[a]=s[a-1]+A[a-1]
print s
for a in range(n,0,-1):
    if s[a]%2==0:
        break
    else:
        count+=1
    print count
if count==n:
    count=-1
    print count
else:
    print count
