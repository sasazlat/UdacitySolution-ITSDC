
# coding: utf-8

# # Identity Matrix
#
# Write a function called identity_matrix that outputs an identity matrix of
# size n.
#
# INPUT
# * n - size of the Identity matrix
#
# OUPUT
# * identity matrix as a list of lists
#
#
# HINTS
# * nested for loops will be helpful
# * the one values are always on the diagonal.  To access diagonal values in a
# list of lists will occur where i = j
# * whenever i does not equal j, the value in the matrix should be 0

# In[ ]:

def identity_matrix(n):
    
    identity = []
    
    # TODO: Write a nested for loop to iterate over the rows and
    # columns of the identity matrix.  Remember that identity
    # matrices are square so they have the same number of rows
    # and columns
    for i in range(n):
        temp_row = []
        for j in range(n):
            if i == j:
                temp_row.append(1)
            else:
                temp_row.append(0)
    # Make sure to assign 1 to the diagonal values and 0 everywhere
    # else
        identity.append(temp_row)
    return identity


# In[ ]:


# TODO: Run this cell to see if your answers are as expected
assert identity_matrix(1) == [[1]]

assert identity_matrix(2) == [[1, 0], 
                             [0, 1]]

assert identity_matrix(3) == [[1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 1]]

assert identity_matrix(4) == [[1, 0, 0, 0],
                             [0, 1, 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]]


# # Multiplication with the Identity Matrix
#
# Copy your matrix multiplication function in the code cell below.  Try
# multiplying a matrix with an identity matrix to prove to yourself that the
# identity matrix is analogous to multiplyin a scalar by one.

# In[ ]:


# TODO: Copy your matrix multiplication function and any other helper
# funcitons here from the previous exercises
def transpose(matrix):
    matrix_transpose = []
    for j in range(len(matrix[0])):
        temp_t = []
        for i in range(len(matrix)):
            temp_t.append(matrix[i][j])
        matrix_transpose.append(temp_t)
    return matrix_transpose


def dot_product(vector_one, vector_two):    
    return sum(i * j for i,j in zip(vector_one, vector_two))


def matrix_multiplication(matrixA, matrixB):
    product = []
    
    ## TODO: Take the transpose of matrixB and store the result
    ##       in a new variable
    matrixB_T = transpose(matrixB)
    
    ## TODO: Use a nested for loop to iterate through the rows
    ## of matrix A and the rows of the tranpose of matrix B
    for matrixA_row in matrixA:
        temp = []
        for matrixB_T_row in matrixB_T:
            temp.append(dot_product(matrixA_row,matrixB_T_row))
    ## TODO: Calculate the dot product between each row of matrix A
    ##         with each row in the transpose of matrix B
    
    ## TODO: As you calculate the results inside your for loops,
    ##       store the results in the product variable
        product.append(temp)
    
    ## TODO:
    return product


# In[ ]:


# TODO: Run this cell to see if your results are as expected.
m = [[5, 9, 2, 4],
     [3, 8, 5, 6],
     [1, 0, 0, 15]]

assert matrix_multiplication(m, identity_matrix(4)) == m
assert matrix_multiplication(identity_matrix(3), m) == m


