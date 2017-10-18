t=input()
while(t>0):
    n=input()
    ans=0
    lis=[int(x) for x in raw_input().split()]
    dic={}
    for a in lis:
        if dic.has_key(a):
            dic[a]+=1
        else:
            dic[a]=1
    for a in dic:
        ans+=dic[a]*(dic[a]-1)
    print ans
    t-=1