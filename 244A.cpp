#include <stdio.h>
using namespace std;
int main()
{
    int n,k;
    scanf("%d%d",&n,&k);
    static bool oranges[1000]={0};
        int children[30]={0};
    for(int i=0;i<k;i++)
    {
        int a;
        scanf("%d",&a);
        oranges[a]=1;
        children[i]=a;
    }
        for(int i=0,j=1;i<k;i++)
        {printf("%d ",children[i]);
            
            for(int z=1;z<n;j++)
            { if(oranges[j]==0) {printf("%d ",j); oranges[j]=1; z++;}
        }    
        printf("\n");
        }
    }