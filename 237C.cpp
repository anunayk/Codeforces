#include<iostream>
#include<fstream>
#include<stdio.h>
#include<algorithm>
#include<cmath>
#include<math.h>
#include<cstring>
#include<string>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<deque>
 
using namespace std;
 
const int MAXN = 1e6 * 2 + 10, SZ = MAXN * 4;
 
typedef vector<int> vi;
vi v(MAXN,1),z(SZ,0);
 
void build(int t,int tl,int tr)
{
    if (tl==tr)
    {
        z[t] = v[tl];
    }
    else
    {
        int tm = (tl+tr)/2;
        build(t*2,tl,tm);
        build(t*2+1,tm+1,tr);
        z[t] = z[t * 2] + z[t * 2 + 1] ;
    }
}
 
int sum(int t,int tl,int tr,int l,int r)
{
    if (l>r) return 0;
    if (tl==l && tr==r) return z[t];
 
    int tm = (tl+tr)/2;
    return sum(t*2, tl, tm, l, min(tm,r)) + sum(t*2+1,tm+1,tr,max(l,tm+1),r);
}
 
int sum(int a,int b)
{
    return z[b] -z[a-1];
}
 
int a,b,k;
 
bool can(int q)
{
    for(int i=a;i<=b-q+1;i++)
    if (sum(i,i+q-1) < k) return false;
    return true;
}
 
int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
 
    cin >> a >> b >> k;
    v[1] = 0;
    v[0] = 0;
    for(int i=2;i<MAXN;i++)
    if (v[i]==1)
    if (i*1ll*i < (long long )MAXN)
    {
        for(int j = i*i;j<MAXN;j+=i)
        v[j] = 0;
    }
 
    //build(1,0,MAXN);
    for(int i=1;i<MAXN;i++) z[i] = z[i-1] + v[i];
 
    int l = 1,r = b-a+1;
    while(r-l>1)
    {
        int t = (l+r)/2;
        if (can(t)) r = t;else l = t;
    }
    if (can(l)) cout << l;
    else
    if (can(r)) cout << r;
    else
    cout << "-1";
}