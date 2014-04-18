/*
Problem

The sum of the squares of the first ten natural numbers is, 
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is, 
(1+2+....+10)^2 = 55^2 + 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

*/

#include <iostream>

using namespace std;

int main()
{
	unsigned long sumsquare, squaresum, difference;
	sumsquare = squaresum = difference = 0;

	//Generate numbers 1-100.  Perform necessary setup calculation.
	for(int i = 0; i <= 100; i++)
	{
		squaresum += i;
		sumsquare += i * i;
	}

	//calculate the final values to be compared.
	squaresum = squaresum * squaresum;

	difference = squaresum - sumsquare;

	cout << "The difference is: " << difference << endl;

	return 0;
};