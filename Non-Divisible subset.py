n,k=raw_input().split()
n=int(n)
k=int(k)
lis=[int(x) for x in raw_input().split()]
lis=lis[:n]
ans=[0]*k
count=0
for no in lis:
    ans[no%k]+=1
for a in range(1,k/2+1):
    count+=max(ans[a],ans[k-a])
count+=min(ans[0],1)
print count
