n=input()
name=[]
dic={}
for _ in xrange(n):
    s=raw_input().strip().split()
    h=s[1]
    s=s[0]
    name.append(s)
    if dic.has_key(h):
        dic[h].append(s)
    else:
        dic[h]=[]
        dic[h].append(s)
l=1
m=0
for key in sorted(dic.iterkeys()):
    print ' '.join(sorted(dic[key])),l,m+len(dic[key])
    l+=len(dic[key])
    m=l-1
    
    
