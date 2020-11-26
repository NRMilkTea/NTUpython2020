//#include <bits/stdc++.h>
#include <iostream>
#include <time.h>
#include <stdlib.h>
using namespace std;

int main(){
	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	
	srand(time(NULL));
	
	int sample = (1 << 14);
	double x, y;
	int in_circle = 0;
	for(int i = 0; i < sample; i++){
		x = double (rand()/(RAND_MAX + 1.0));
		y = double (rand()/(RAND_MAX + 1.0));
		if (x*x + y*y <= 1.0) in_circle ++;
	}
	cout << (4.0 * in_circle) / sample << endl;

	return 0;
}


