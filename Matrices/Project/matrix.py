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
        return sum(self.g[i][i] for i in range(self.h))

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
        ## Check if matrix is 1x1 or 2x2.
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
        return Matrix(inverse)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        for j in range(self.w):
            temp_t = []
            for i in range(self.h):
                temp_t.append(self.g[i][j])
            matrix_transpose.append(temp_t)
        return Matrix(matrix_transpose)

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
        # write a for loop within a for loop to iterate over
        # the matrices
        for m in range(self.h):
            # matrix to hold a row for appending sums of each element
            row = []
            for n in range(self.w):
                row.append(self.g[m][n] + other.g[m][n])
            matrixSum.append(row)
        return Matrix(matrixSum)

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
        matrixNeg = []    
        # write a for loop within a for loop to iterate over
        # the matrices
        for m in range(self.h):
            # matrix to hold a row
            row = []    
            for n in range(self.w):
                row.append(-(self.g[m][n]))
            matrixNeg.append(row)
        return Matrix(matrixNeg)


    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtituted if the dimensions are the same") 
        #
        # TODO - your code here
        #
        matrixSub = []    
        # write a for loop within a for loop to iterate over
        # the matrices
        for m in range(self.h):
            # matrix to hold a row for appending sums of each element
            row = []
            for n in range(self.w):
                row.append(self.g[m][n] - other.g[m][n])
            matrixSub.append(row)
        return Matrix(matrixSub)


    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        if self.w != other.h:
            raise(ValueError, "Matrices can only be multiplied  if the dimensions of columns of the first and rows of the second are the same ") 
        
        # Transpose other matrix
        other_T = other.T()
        # Dot product of two vectors of 1xn dimensions
        def dot_product(vector_one, vector_two):    
            return sum(i * j for i,j in zip(vector_one, vector_two))
        #
        # TODO - your code here
        #
        matrixMul = []    
        # matrix to hold a row for appending sums of each element
        for self_row in self.g:
            temp = []
            for other_T_row in other_T.g:
                temp.append(dot_product(self_row,other_T_row))
            matrixMul.append(temp)

        return Matrix(matrixMul)


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
            #   
            # TODO - your code here
            #
            matr = []
            for r in self.g:
                row = []
                for c in r:
                    row.append(other * c)
                matr.append(row)
            return Matrix(matr)

            
