#include <iostream>
#include <vector>
#include <string.h>
 
using namespace std;
 
int main()
{
    int n,q;
        cin >> n >> q;
        vector<char> vec;
        char str[101];
        cin >> str;
        for(int i=0;i<strlen(str); i++)
                vec.push_back(str[i]);
        for(int i=0; i<n ;i++)
        {
                int output[10];
                memset(output,0,sizeof(output));
                int l,r;
                cin >> l >> r;
                vector<char> cur(vec.begin()+l-1, vec.begin()+r);
                int idx = 0;
                char dp = '>';
                while(true)
                {
                        if (cur[idx]>='0' && cur[idx] <='9')
                        {
                                int temp = cur[idx]-'0';
                                output[temp]++;
                                if (temp == 0)
                                {
                                        cur.erase(cur.begin()+idx);
                                }
                                else
                                {
                                        temp--;
                                        cur[idx] = temp + '0';
                                }
                        }
                        else 
                        {
                                if (dp == '>' && idx > 0 && cur[idx-1] == '>')
                                {
                                        cur.erase(cur.begin()+idx-1);
                                }
                                else if (dp =='<' && idx<cur.size()-1 && cur[idx+1] == '<')
                                {
                                        cur.erase(cur.begin()+idx+1);
                                }
                                dp = cur[idx];
                        }
                        if (dp == '>')
                        {
                                idx++;
                                if (idx==cur.size())
                                        break;
                        }
                        else
                        {
                                idx--;
                                if (idx<0)
                                        break;
                        }
                }
                for(int i=0; i<10; i++)
                {
                        cout << output[i] << " ";
                }
                cout << endl;
        }
 
        return 0;
}