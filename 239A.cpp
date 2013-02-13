#include<iostream>

using namespace std;

int main()
    {
        long int y, k, n, x, found=0;
        
        cin >> y >> k >> n;
        
        x = y % k;
        x = k-x;
        x = x + y;
        
        while (x <= n)
            {
                cout << x-y << " ";
                x += k;
                found = 1;
            }
        
        if (found == 0)
            {
                cout << -1;
            }
        
        return 0;
    }