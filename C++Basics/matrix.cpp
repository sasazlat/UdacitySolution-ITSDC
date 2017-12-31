#include "matrix.h"

Matrix::Matrix() {
	std::vector <std::vector <float> > initial_grid(10, std::vector <float>(5, 0.5));
	grid = initial_grid;
	rows = initial_grid.size();
	cols = initial_grid[0].size();

}

Matrix::Matrix(std::vector <std::vector <float> > initial_grid) {
	grid = initial_grid;
	rows = initial_grid.size();
	cols = initial_grid[0].size();
}


void Matrix::setGrid(std::vector< std::vector<float> > new_grid) {
	grid = new_grid;
	rows = new_grid.size();
	cols = new_grid[0].size();
}

std::vector< std::vector<float> > Matrix::getGrid() {
	return grid;
}

std::vector<int>::size_type Matrix::getRows() {
	return rows;
}

std::vector<int>::size_type Matrix::getCols() {
	return cols;
}



/* TODO: Define a matrix_addition function
**   INPUT: a matrix
**   OUPUT: the sum of the grid variable and the input matrix
**
** STEPS:
**  1. check that the matrix in the grid variable
**     and the input matrix have the same size
**
**     if not, throw an error like
**         throw std::invalid_argument("matrices are not the same size");
**
** 2. add the matrices together and return
**       the result as a Matrix. You can do this part
**       with nested for loops. If you use an intermediate
**       vector to store a row, the vector.clear()
**       method might be useful.
**
*/
Matrix Matrix::matrix_addition(Matrix matrix)
{


	if (rows != matrix.getRows() && cols != matrix.getCols())
	{
		std::cout << "Matrices are not the same" << std::endl;
		throw std::invalid_argument("Matrices are not the same size");
		exit(0);
	}
	std::vector< std::vector<float> > result;
	std::vector< std::vector<float> > temp_grid = matrix.getGrid();
	for (size_t i = 0; i < getRows(); i++)
	{
		std::vector<float> temp_row;
		for (size_t j = 0; j < getCols(); j++)
		{
			temp_row.push_back(grid[i][j] + temp_grid[i][j]);
		}
		result.push_back(temp_row);
		temp_row.clear();
	}

	return Matrix(result);
}

/* TODO: Define a matrix_print function
** This function has no inputs and no outputs
** The purpose of the function is to display the matrix in
** the terminal using std::cout.
**
**
** The output should look something like:
** 4    9   1   10
** 5    11  6   17
** 8    4   15  2
*/
void Matrix::matrix_print(void)
{
	for (size_t i = 0; i < getRows(); i++)
	{
		for (size_t j = 0; j < getCols(); j++)
		{
			std::cout << grid[i][j] << "\t";
		}

		std::cout << "" << std::endl;
	}
}

Matrix Matrix::matrix_transpose() {
	std::vector< std::vector<float> > new_grid;
	std::vector<float> row;

	for (int i = 0; i < cols; i++) {
		row.clear();

		for (int j = 0; j < rows; j++) {
			row.push_back(grid[j][i]);
		}
		new_grid.push_back(row);
	}

	return Matrix(new_grid);
}
