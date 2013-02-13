#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
int m,k;
cin>>m>>k;
int i;
int s[1100],d[1100];
for(i=0;i<m;i++)cin>>d[i];
for(i=0;i<m;i++)cin>>s[i];
 
int time = 0;
int start = 0;
int fuel = 0;
while(start!=m)
{
fuel += s[start];
if(fuel<d[start])
{
time+=k;
fuel+=s[start];
continue;
}
fuel-=d[start];
time+=d[start];
start++;
}
cout<<time;
return 0;
}