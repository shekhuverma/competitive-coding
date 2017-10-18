n=input()
dic={}
dic2={}
lis=[]
count=0
for a in xrange(n):
    temp=raw_input().strip().split()
    if dic.has_key(temp[0]):
        if dic[temp[0]].has_key(temp[1]):
            dic[temp[0]][temp[1]]+=1
        else:
            dic[temp[0]][temp[1]]=1
    else:
        dic[temp[0]]={}
        dic[temp[0]][temp[1]]=1
print dic
for key in sorted(dic.iterkeys()):
    if len(dic[key])==2:
        count+=min(dic[key]['L'],dic[key]['R'])
print count

