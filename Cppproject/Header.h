#pragma once



#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include<cstdio>
#include<cstddef>


using namespace std;


int calculate(float input1, float input2, char operation, float &result);
void printEquation(float input1, float input2, char operation, float &result);


int calculate(float input1, float input2, char operation, float &result) {
	if (operation == '+') { return result = input1 + input2; }
	else if (operation == '-') { return result = input1 - input2; }
	else if (operation == '*') { return result = input1*input2; }
	else if (operation == '/') { return result = input1 / input2; }
}
void printEquation(float input1, float input2, char operation, float &result) {
	std::cout << input1 << operation << input2 << "=" << result;
}