#include <iostream>
#include <stack>
#include <queue>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <vector>
#define fi first
#define se second
using namespace std;
int n,x,l,c,k=0;
bool y[500][500];
bool found;
int main(){
        cin >> n;
        memset(y,0,sizeof(y));
        x = 100;
        l = 1;
        while(n){
                
                 c = (x*(x-1)*(x-2))/6;
                while (c>n){
                        x--;
                        c = (x*(x-1)*(x-2))/6;
                }
                n-=c;
                for (int i = 0; i <x;i++){
                        for (int j = 0; j <x; j++){
                                if (l+i == l+j) continue;
                                y[l+i][l+j] = 1;
                                y[l+j][l+i] = 1;
                        }
                        
                }
                l+=x;
        }
        for (int i = 1; i < 101; i++)
{
                found = true;
                for (int j = 1; j < 101; j++){
                        if (y[i][j] != false)
                                {
                                        found = false;
                                        break;
                                }
                }
                if (found == true)
                        {
                                k = i;
                                break;
                        }
                }
        cout << k-1 << endl;
        for (int i = 1; i < k; i++)
{
                for (int j = 1; j < k; j++){
                        printf("%d",y[i][j]);
                }
                printf("\n");
        }
}