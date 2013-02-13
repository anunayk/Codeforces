#include<iostream>
#define mod 1073741824

using namespace std;

long NumOfDivisors(long num)
{
	long count=0, i;
	
	for (i=1; i*i<=num; i++)
		{
			if (num % i == 0)
				{
					count++;
					if (num/i != i)
					{
						count++;
					}
				}
		}
	return count;
}

long compute(int a, int b, int c)
{
	int i, j, k;
	long ans=0;
	for (i=1; i<=a; i++)
		{
			for (j=1; j<=b; j++)
				{
					for (k=1; k<=c; k++)
						{
							ans = (ans + NumOfDivisors(i*j*k)) % mod;
						}
				}
		}
	return ans;
}

int main()
	{
		int a, b, c;
		cin >> a >> b >> c;

		cout << compute(a, b, c);
		return 0;
	}