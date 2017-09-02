#include <iostream>
using namespace std;
int main()
{
    int n,c=0;
    int common=0;
    int temp[100][26]={};
    cin>>n;
    int counter=0;
    while(c<n)
    {
        int len;
        string s;
        cin>>s;
        len=s.length();
        for(int i=0;i<len;i++)
        {
            (temp[c][s[i]-'a'])++;
        }
        c++;
    }
    for(int k=0;k<26;k++)
    {
        for(int i=0;i<n;i++)
        {
            if(temp[i][k]!=0)
            {
                counter=1;
            }
            else
            {
                counter=0;
                break;
            }

        }
        common=common+counter;
    }
    cout<<common;
    return 0;
}
