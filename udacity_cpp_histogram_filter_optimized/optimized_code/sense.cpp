#include "headers/sense.h"

using namespace std;

// OPTIMIZATION: Pass larger variables by reference
vector< vector <float> > sense(char color, vector< vector <char> > &grid, vector< vector <float> > &beliefs, float p_hit, float p_miss)
{
	// OPTIMIZATION: Is the newGrid variable necessary?
	// Could the beliefs input variable be updated directly?

	int i, j;
	const int height = grid.size();
	const int width = grid[0].size();

	for (i = 0; i < height; i++) {
		for (j = 0; j < width; j++) {
			// OPTIMIZATION: Which of these variables are 	needed?
			beliefs[i][j] = ((grid[i][j] == color) ? p_hit : p_miss) * beliefs[i][j];
		}
	}
	return beliefs;
}
