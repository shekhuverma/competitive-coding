import sys,math
s =raw_input().strip()
l=len(s)
row=int(math.floor(math.sqrt(l)))
col=int(math.ceil(math.sqrt(l)))
for j in range(0,col):
    for i in range(j,l,col):
        sys.stdout.write(str(s[i]))
    sys.stdout.write(" ")