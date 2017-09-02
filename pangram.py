#pangram
res=[[0]*26];
sen=raw_input("Enter the sentence").lower()
for ele in sen:
    if ele==" ":
        continue
    else:
        temp=ord(ele)-97
        res[0][temp]+=1
for i in range(0,26):
    if(res[0][i]!=0):
        bol=1
    else:
        bol=0
        print("Not a paragram")
        break;
if(bol==1):
    print("Paragram")
