/*
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

Numbers contained in input.txt

*/

#include <iostream>
#include <fstream>
#include <list>
#include <string>


using namespace std;

int main()
{
	const int length = 50;
	const int height = 100;
	int numbers[height][length], temp, temp1;
	string intemp;
	list<int> solution;
	int carryover = 0;
	
	ifstream in;
	in.open("input.txt", ios::in);
	if(in.is_open()){cout << "File open successful" << endl;} else {cout << "Unsuccessful" << endl; return 1;}
	cout << "This program will sum the following 100 50 digit numbers. " << endl;
	for(int i = 0; i < height; i++)
	{
		in >> intemp;
		cout << intemp << endl;
		for(int j = 0; j < length; j++)
		{
			numbers[i][j] = intemp.at(j) - '0';
		}
	}

	for(int i = (length - 1); i >= 0; i--)
	{
		temp = 0;
		for(int j = 0; j < height; j++)
		{
			temp += numbers[j][i];
		}
		temp1 = temp + carryover;
		temp = temp1;
		while(temp1 > 9)			//will cut off one length of number until last remaining digit is found.
		{	temp1 = temp1 % 10;	}
		solution.push_back(temp1);
		temp = temp / 10;			//cuts off last digit that was stored previously.
		carryover = temp;
	}

	solution.push_back(carryover % 10); carryover = carryover / 10;
	solution.push_back(carryover % 10); carryover = carryover / 10;		//adds the two digits of remaining carryover to the number.

	cout << "The solution is: " << endl;

	list<int>::iterator i;
	solution.reverse();
	for(i=solution.begin(); i != solution.end(); ++i) cout << *i << " ";
	cout << endl;
	return 0;
};