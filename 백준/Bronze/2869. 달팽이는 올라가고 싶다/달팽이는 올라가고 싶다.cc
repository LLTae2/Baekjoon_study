#include<iostream>
#include<cmath>
using namespace std;
int A, B, V;
int main(){
	cin>>A>>B>>V;
	printf("%.f", ceil((double)(V-B)/(A-B)));
	return 0;
}