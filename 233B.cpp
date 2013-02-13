#include<iostream>
using namespace std;
unsigned long long int sqrt(long long int n){
unsigned long long int low=1,high=1000000000,temp;
        while(low<high){
                temp=(low+high)/2;
                if(temp*temp<n){
                        low=temp+1;
                }
                else if(temp*temp==n)
                return temp;
                else{
                        high=temp-1;
                }
        }
        return low;
}
int sumof(long long int n){
        int sum=0;
        while(n){
                sum+=n%10;
                n/=10;
        }
        return sum;
}
int main(){
        unsigned long long int n,k,s;
        cin>>n;
        for(k=81;k>0;k--){
                s=sqrt(k*k+4*n);
                if(s*s==k*k+4*n&&sumof((s-k)/2)==k){
                        n=(s-k)/2;
                        break;
                }
        }
        if(k==0)
        cout<<"-1"<<endl;
        else
        cout<<n<<endl;
        return 0;
}