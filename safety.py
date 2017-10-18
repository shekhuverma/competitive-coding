# -*- coding: utf-8 -*-
import string
s=raw_input()
n=input()
for _ in xrange(n):
    comm=[int(x) for x in raw_input().strip().split()]
    if len(comm)==4:
        i=comm[1]-1
        j=comm[2]-1
        k=comm[3]-1
    if len(comm)==3:
        i=comm[1]-1
        j=comm[2]-1
    if comm[0]==1:
        if s[i:j+1]==s[k:k+j-i+1]:
            print "Y"
        else:
            print "N"
    if comm[0]==2:
        for a in xrange(i,j+1):
            s=list(s)
            s[i+a-1]=s[k+a-1]
    if comm[0]==3:
        for a in xrange(i,j):
            if s[a]=="z":
                s[a]="a"
            else:
                s[a]=chr((ord(str(s[a]))+1))
        s=str(s)
        
            
