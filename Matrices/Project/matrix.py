import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            if (a * d - b * c) == 0:
                raise ValueError('The denominator of a fraction cannot be zero')
            else:
                return a * d - b * c

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        return self.g[0][0] + self.g[1][1]

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

            # TODO - your code here
        inverse = []
        ## TODO: Check if matrix is 1x1 or 2x2.
        ## Depending on the matrix size, the formula for calculating
        ## the inverse is different
        if len(self.g) == 1:
            inverse.append([1. / self.g[0][0]])
        else:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            if (self.determinant()) == 0:
                raise ValueError('The denominator of a fraction cannot be zero')
            else:
                detA = self.determinant()
                inverse = [[d / detA, -b / detA],[-c / detA, a / detA]]

    
        ## TODO: Calculate the inverse of the square 1x1 or 2x2 matrix.
    
        return inverse

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        for j in range(self.h):
            temp_t = []
            for i in range(self.w):
                temp_t.append(self.g[i][j])
            matrix_transpose.append(temp_t)
        return matrix_transpose

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #
        # TODO - your code here
        #
        # initialize matrix to hold the results
        matrixSum = []
    
        # matrix to hold a row for appending sums of each element
        row = []
    
        # TODO: write a for loop within a for loop to iterate over
        # the matrices
        for m in range(self.w):
            for n in range(self.h):
                row.append(self.g[m][n] + other[m][n])
        # TODO: As you iterate through the matrices, add matching
        # elements and append the sum to the row variable
    
        # TODO: When a row is filled, append the row to matrixSum.
        # Then reinitialize row as an empty list
            matrixSum.append(row)
            row = []
        return matrixSum

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #
        # TODO - your code here
        #

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #
        # TODO - your code here
        #

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #
        # TODO - your code here
        #

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            
