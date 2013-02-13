#include<cstdio>
#include<vector>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
#include<sstream>
#include<bitset>
#include<deque>
#include<utility>
#include<cstdlib>
#include<iomanip>
#include<cctype>
#include<climits>
#include<iostream>
#ifndef ONLINE_JUDGE
#include<conio.h>
#endif
using namespace std;
#define ll long long
#define ull unsigned long long
#define max(x,y)(x>y?x:y)
#define min(x,y)(x<y?x:y)
#define equa(x,y)(x==y?1:0)
#define all(x) x.begin(),x.end()
#define vi  vector<int>
#define vvi vector<vector<int> >
#define vil vector<long long>
#define vvil vector<vector<long long> >
#define inpint(x) scanf("%d",&x)
#define inpll(x) scanf("%lld",&x)
#define inpull(x) scanf("%ull",&x)
#define inpstr(x) scanf("%s",x)
#define gcd __gcd
#define INF 2147483647
string tostr(long long x) { stringstream ss; ss << x; return ss.str(); }
long long toint(const string &s) { stringstream ss; ss << s; long long x; ss >> x; return x; }
#define fo(x,y,z) for(int x=y;x<=z;x++)
#define re(x,y,z) for(int x=y;x>=z;x--)
#define LIMIT 1000
#define mod 1000000007
vector<int> pri;
void sieve(){vector < bool > prime ( LIMIT + 1 , true ) ;prime [ 0 ] = prime [ 1 ] = false ;for ( int i = 2 ; i <= LIMIT ; ++ i )if ( prime [ i ] )if ( i * 1ll * i <= LIMIT )for ( int j = i * i ; j <= LIMIT ; j += i )prime [ j ] = false ;for(int i=2;i<=LIMIT;i++)if(prime[i])pri.push_back(i);}
string s;
int len,ar[10][10]={0};
set<ll> v;
void rec(string num,int i,int j)
{
    if(toint(num)>1LL*1000000000)return ;
        rec(num+tostr(i),i,j);
        rec(num+tostr(j),i,j);
        v.insert(toint(num));
}
void pre()
{
        fo(i,1,9)
        fo(j,0,9)
        rec(tostr(i),i,j);
 
}
int main()
{
#ifndef ONLINE_JUDGE
freopen("input.txt","r",stdin);
freopen("outpu.txt","w",stdout);
#endif
pre();
int n;
cin>>n; 
int i=0;
set<ll>::iterator it;
for(it=v.begin();it!=v.end();it++)
        if(*it>n)break;
        else i++;
cout<<i<<endl;
#ifndef ONLINE_JUDGE
        getch();
#endif
return 0;
}