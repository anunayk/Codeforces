#include <iostream>
#include <algorithm>
#define DN 100005
using namespace std;
 
long long sp[DN];
int n,k,sir[DN];
 
int check(int nr) {
    for(int i=nr; i<=n; ++i) {
        long long sum=sp[i]-sp[i-nr];
        if(nr*1LL*sir[i]-sum<=k) {
            //cout<<nr*1LL*sir[i]<<' '<<sum<<'\n';
            return sir[i];
        }
    }
    return 0;
}
 
int main()
{
    cin>>n>>k;
    for(int i=1; i<=n; ++i) {
        cin>>sir[i];
    }
    sort(sir+1,sir+n+1);
    for(int i=1; i<=n; ++i) sp[i]=sp[i-1]+sir[i];
    int ls=1,ld=n,rez=0;
    for(;ls<=ld;) {
        int m=(ls+ld)/2;
        if(check(m)) {
            rez=m;
            ls=m+1;
        }else ld=m-1;
    }
    cout<<rez<<' '<<check(rez);
    return 0;
}