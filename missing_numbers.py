#missing numbers
list1=[]
list2=[]
n= int(raw_input(""))
word1={}
word2={}
list1=sorted([int(x) for x in raw_input().split()])
list1=list1[0:n]
for i in list1:
    if i in word1:
        word1[i]+=1
    else:
        word1[i]=1
m=int(raw_input(""))
list2=sorted([int(x) for x in raw_input().split()])
list2=list2[0:m]
for i in list2:
    if i in word2:
        word2[i]+=1
    else:
        word2[i]=1
for i in word2:
    if word1[i]<word2[i]:
        print i,
    else:
        continue
