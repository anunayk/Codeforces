#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<set>
#include<map>
#include<utility>
#include<climits>

#define unsigned long long int ulli
# define FRm(i, m, n)     for( int i = m; i <=n; i++)
# define FRrev(i, n)         for( int i = n; i >= 0; i-- )
# define FRrevm(i,n,m)         for( int i = n; i >= m; i-- )
#define max(a,b) ((a)>(b)?(a):(b))
#define S(a) scanf("%d",&(a))
#define P(a) printf("%d",(a))
#define min(a,b) ((a)<(b)?(a):(b))
#define NL printf("\n")
#define sqr(a) ((a)*(a))
#define SL(a) scanf("%lld",&(a))
#define PL(a) printf("%lld",(a))
#define lli long long int
#define FOR(I,A,B) for(int I= (A); I<(B); ++I)
#define inarrd(arr,n) for(int i=0;i<n;i++)S(arr[i]);
#define outarrd(arr,n) for(int i=0;i<n;i++){PFd(arr[i]);PF(" ");}NL;
#define outarrN(arr,n) for(int i=0;i<n;i++){PFd(arr[i]);PFN;}
using namespace std;
int main()
{
    int n,c,l,k,i;
    S(n);
    c=0;
    l=0;
    k=0;
    i=1;
    int arr[n];
    vector<int>ans;
    inarrd(arr,n);
    while(i<=n)
    {
        if(arr[i-1]<0)
            c++;
        if(c==3 )
        {
            ans.push_back(i-1-l);
            l=i-1;
            k++;
            c=0;
            continue;            
        }
        if(i==n)
        {
           ans.push_back(i-1-l); 
           k++;
        }
        i++;
    }
    P(k);NL;
    FOR(i,0,ans.size()-1)
    {
         cout<<ans[i]<<" ";
    }
    
    cout << ans[ans.size()-1]+1;
}