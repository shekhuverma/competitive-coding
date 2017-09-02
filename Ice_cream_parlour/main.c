#include<stdio.h>
//#include<conio.h>
#include<stdlib.h>
void print(int list[],int n) //just to see lists are getting stored or not
{
    int i=1;
    for(i;i<=n;i++)
    {
        printf("%d",list[i]);
    }
}
int main()
{
    int t,n,m,k;
    int i=0;
    int j=0;
    scanf("%d",&t);
    while(j<t)
    {
        int list[10000];
        n=0;
        m=0;
        scanf("\n%d",&m);
        scanf("\n%d",&n);
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&list[i]);
        }
        for(i=1;i<=n;i++)
        {
            for(k=1;k<=n;k++)
            {
                if(i<k)
                {
                    if(list[i]+list[k]==m)
                    {
                        printf("%d %d",i,k);
                        break;
                    }
                }
            }
        }
        printf("\n");
        j++;
    }
    return 0;
}
