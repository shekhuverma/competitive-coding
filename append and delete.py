s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())
diff=0
ls=len(s)
lt=len(t)
ans=False
if ls<lt:
    l=ls
else:
    l=lt
for i in range(0,l):
    if s[i]==t[i]:
        diff+=1
    else:
        break
diff=(ls+lt)-(2*diff)
if (diff<=k and diff%2==k%2) or ls+lt<k:
    ans=True
if(ans):
    print "Yes"
else:
    print "No"
