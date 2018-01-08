#include "headers/initialize_beliefs.h"

using namespace std;

// OPTIMIZATION: pass large variables by reference
vector< vector <float> > initialize_beliefs(vector< vector <char> > &grid) {

	// OPTIMIZATION: Which of these variables are necessary?
	// OPTIMIZATION: Reserve space in memory for vectors

	const int height = grid.size();
	const int width = grid[0].size();
	static float prob_per_cell = 1.0 / ((float)height * width);

	// OPTIMIZATION: Is there a way to get the same results 	// without nested for loops?
	vector< vector <float> > newGrid(grid.size(), vector<float>(grid[0].size(), 1.0 / ((float)height * width)));
	
	return newGrid;
}