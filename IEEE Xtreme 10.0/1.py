n,k=raw_input().split()
n,k=int(n),int(k)
dic={}
for a in range(n):
    temp=input()
    if dic.has_key(temp):
        dic[temp]+=1
    else:
        dic[temp]=1
print dic
if len(dic)==k:
    ans=0
else:
    ans=dic[max(dic)]-dic[min(dic)]    
