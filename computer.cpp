#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;
int main(int argc, char** argv) {
	cout<< "Hello,I'm a computer. \n" ;
	float a,b,sum;
	printf("Enter the two number here, I will add them up.\n");
	cin>> a ;
	cin>> b ;
	sum=a+b;
	printf("%f + %f = %f\n" ,a,b,sum );
	printf("Again!enter the two number here, I will Subtract them up.\n");
	float c,d;
	cin>> c ;
	cin>> d ;
	sum=c-d;
	printf("%f - %f = %f\n" ,c,d,sum);
	printf("Again!enter the two number here, I will Multiply them up.\n");
	float e,f;
	cin>> e ;
	cin>> f ;
	sum=e*f;
	printf("%f * %f = %f\n" ,e,f,sum);
	printf("Again!enter the two number here, I will Divide them up.\n");
	float g,h;
	cin>> g ;
	cin>> h ;
	sum=g/h;
	printf("%f / %f = %f\n" ,g,h,sum);
}
