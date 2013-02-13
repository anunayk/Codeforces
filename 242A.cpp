#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x,y,a,b,i,j,count = 0,sum = 1;
    scanf("%d %d %d %d",&x,&y,&a,&b);
    
    for(i = b ; i <= y ; i++)
    {
        for(j = a ; j <= x ; j++)
        {
            if(j > i)
                count++;
        }
    }
    
    printf("%d\n",count);
    
    for(j = a ; j <= x ; j++)
    {
        for(i = b ; i <= y ; i++)
        {
            if(j > i)
                printf("%d %d\n",j,i);
        }
    }
    
    return 0;
}