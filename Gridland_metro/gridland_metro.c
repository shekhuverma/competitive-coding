//gridland metro
#include<stdio.h>
typedef long long ll;
int main()
{
    ll list1[3];
    ll i,j,m,n;
    int k;
    ll ans=0;
    ll temp[100000];
    ll r,c1,c2;
    i=0;
    j=0;
    scanf("%lld %lld %d",&m,&n,&k);
    while(j<k)
    {
        scanf("%lld %lld %lld",&r,&c1,&c2);
        temp[r]=temp[r]+c2-c1+1;
        ans+=temp[r];
        j++;
    }
    ans=(n*m)-ans;
    printf("%lld",ans);
    return 0;
}
