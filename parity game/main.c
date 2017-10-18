//https://www.hackerrank.com/contests/hourrank-22/challenges/parity-game
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
int main()
{
    int n;
    scanf("%i", &n);
    int *a = malloc(sizeof(int) * n);
    int *s = calloc(n+1,sizeof(int));
    for(int A_i = 0; A_i<n; A_i++)
    {
       scanf("%d",&a[A_i]);
       s[A_i+1]=s[A_i]+a[A_i];
    }
    for(int A_i=0; A_i<n; A_i++)
    {
       scanf("%d",s[A_i]);
    }
    return 0;
}
