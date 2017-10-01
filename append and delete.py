s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())
count=0
i=0
ls=len(s)
lt=len(t)
ans=False
if s==t:
    ans=True
while(s[i]==t[i]):
    i+=1
    if ans==True:
        break
count=(ls+lt)-(2*i)
if (count<=k and count%2==k%2):
    ans=True
if(ans):
    print "Yes"
else:
    print "No"
