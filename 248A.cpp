#include <iostream>
#include <algorithm>
using namespace std ;
int main() {
    int l0,l1,r0,r1;
    l0=l1=r0=r1=0;
    int t ;
    int l, r;
    cin >> t ;
    while ( t-- ) {
        cin >> l >> r ;
        if ( l == 0 )
            l0++ ;
        if ( l == 1 )
            l1++ ;
        if ( r == 0 )
            r0++ ;
        if ( r == 1 )
            r1++ ;
    }
        cout << min ( l0, l1 ) + min ( r0, r1 ) << endl;
    return 0 ;
}