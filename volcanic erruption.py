n = int(raw_input().strip())
m = int(raw_input().strip())
mmm=[]
lis=[[0 for x in xrange(n)] for x in xrange(n)]
for a0 in xrange(m):
    x, y, w = raw_input().strip().split(' ')
    x, y, w = [int(x), int(y), int(w)]
    for a in xrange(w,0,-1):
        for b in xrange(10,20):
            for c in xrange(4,31):
                lis[c][b]+=1
        mmm=max(lis[c][b])
        mm.append(mmm)
print max(mmm)
                    
