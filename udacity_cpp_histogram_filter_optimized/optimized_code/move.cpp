#include "headers/move.h"
//#include "headers/zeros.h"

using namespace std;

// OPTIMIZATION: Pass large variable by reference
void move(int dy, int dx, 
	vector < vector <float> > &beliefs) 
{
	const int height = beliefs.size();
	const int width = beliefs[0].size();

	//vector < vector <float> > newGrid;
  
  	// OPTIMIZATION: Use improved zeros function
	//newGrid = zeros(height, width);

// OPTIMIZATION: Eliminate any variables that aren't needed
	//vector <float>  newRow;
		
  	for (int i=0; i<height; i++) {
		for (int j=0; j<width; j++) {
			int new_i = (i + dy + height) % height;
			int new_j = (j + dx + width)  % width;			
			beliefs[new_i][new_j] = beliefs[i][j];
		}
	}
}
