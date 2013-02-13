#include<cstdio>
#include<cmath>

using namespace std;

char ans(long xa, long ya, long xb, long yb, long xc, long yc)
	{
		float m, c, da, db;
		if ((xa - xb) != 0)
			{
				m = (float) (ya - yb) / (xa - xb);
				c = (float) (yc - ya - m*(xc - xa));
			}
		else
			{
				c = xc - xb;
			}
		
//		da = (float) sqrt(pow(xa, 2) + pow(ya, 2));
//		db = (float) sqrt(pow(xb, 2) + pow(yb, 2));
		
		if (c == 0)
			{
				return 'T';
			}
		else if (c > 0)
			{
				if (yb > ya)
					{return 'R';}
				else if (yb < ya)
					{return 'L';}
				else
					{
						if (xb > xa)
						{
							return 'R';
						}
						else
						{
							return 'L';
						}
					}
			}
		else
			{
				if (yb > ya)
					{return 'L';}
				else if (yb < ya)
					{return 'R';}
				else
					{
						if (xb > xa)
						{
							return 'L';
						}
						else
						{
							return 'R';
						}
					}
			}
	}

int main()
	{
		long xa, ya, xb, yb, xc, yc;
		scanf("%ld", &xa);
		scanf("%ld", &ya);
		scanf("%ld", &xb);
		scanf("%ld", &yb);
		scanf("%ld", &xc);
		scanf("%ld", &yc);
		
		char c = ans(xa, ya, xb, yb, xc, yc);
		
		if (c == 'T')
			{
				printf("TOWARDS");
			}
		else if (c == 'L')
			{
				printf("LEFT");
			}
		else
			{
				printf("RIGHT");
			}
		
		return 0;
	}