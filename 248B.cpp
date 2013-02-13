#include <iostream>

using namespace std;

int modulo(int n)
    {
        int i, ans = 10;
        for (i=1; i<n; i++)
            {
                ans = (ans * 10) % 210;
            }
        return ans;
    }

int main() {
	int n, i, m;
    cin >> n;
    if ((n == 1) || (n == 2))
        {
            cout << -1;
        }
    else if (n == 3)
        {
            cout << 210;
        }
    else
        {
            m = 210 - modulo(n-1);
            if (m < 10)
                {
                    cout << 1;
                    for (i=1; i<n-1; i++)
                        {
                            cout << 0;
                        }
                    cout << m;
                }
            else if (m < 100)
                {
                    cout << 1;
                    for (i=1; i<n-2; i++)
                        {
                            cout << 0;
                        }
                    cout << m;
                }
            else
                {
                    cout << 1;
                    for (i=1; i<n-3; i++)
                        {
                            cout << 0;
                        }
                    cout << m;
                }
        }
        
	return 0;
}