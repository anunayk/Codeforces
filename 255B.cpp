#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
 
using namespace std;
 
int main()
{
    string s="";int found;
    cin>>s;
 
    for(int k=0;k<s.length();k++)
    {
        found = s.find("yx");
        
        if (found!=string::npos)
        {
            s[found] ='x';
            s[found+1] ='y';
 
        }
    }
    for(int k=0;k<s.length();k++)
    {
        found = s.find("xy");
        
        if (found!=string::npos)
        {
            s.erase(found,2);
 
        }
    }
 
 
    cout << s << endl;
    return 0;
}