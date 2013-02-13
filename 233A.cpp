#include<stdio.h>
int main()
{
        int n,i;
        scanf("%d",&n);
        if (n%2==1) printf("-1\n");
        else {
                printf("2");
                for (i=2;i<=n;i++) {
                        if (i%2==0) printf(" %d",i-1);
                        else printf(" %d",i+1);
                }
                printf("\n");
        }
        return 0;
}