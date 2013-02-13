#include<iostream>

using namespace std;

int main()
{
	long n, ans, a, b, c;
	cin >> n;
	
	a = n * (n-1) * (n-2);
	b = n * (n-1) * (n-2) / 2;
	c = (n-1) * (n-2) * (n-3);
	
	if (n < 3)
		{
			if (n == 1)
				{
					cout << 1;
				}
			if (n == 2)
				{
					cout << 2;
				}
		}
	else {
		if (n % 2 == 0)
		{
			if (b > c)
				{
					cout << b;
				}
			else
				{
					cout << c;
				}
		}
		else
		{
			cout << a;
		}
	}
	
	
}