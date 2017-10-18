
import sys
def howManyGames(p, d, m, s):
    count=0
    temp=0
    for a in range(p,m,-d):
        temp+=a
        if temp>=s:
            break
        else:
            count+=1
    while(temp+m<=s):
        temp+=m
        count+=1
    return temp
if __name__ == "__main__":
    p, d, m, s = raw_input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    ans=howManyGames(p, d, m, s)
    print ans
