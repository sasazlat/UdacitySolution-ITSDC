/*Goal: practice searching an array in C++
**There is an array of integers. The length of the arrays to be searched
**varies. A user will enter an integer and the program will search the array.
**If the value is in the array, the program will return the location of
**the element. If the value is not in the array, the user will be notified
**that the value is not in the array. To exit the program the user will enter -1.
*/

#include"Header.h"

int main()
{
	char operation = '*';
	float input1 = 9.8;
	float input2 = 2.3;
	float result = 0;

	calculate(input1, input2, operation, result);
	printEquation(input1, input2, operation, result);
	return 0;
}
