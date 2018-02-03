#gridland metro
ip=[int(x) for x in raw_input().split()]
temp={}
j=0
ans=0
while(j<ip[2]):
    ip1=[int(y) for y in raw_input().split()]
    r=ip1[0]
    c1=ip1[1]
    c2=ip1[2]
    if temp.has_key(r):
        temp[r].extend([c1,c2])
    else:
        temp[r]=[c1,c2]
    j+=1
print temp
##for key,value in temp.iteritems():
##    for a in range(len(value)):
##        frm=a
##        till=a+1
