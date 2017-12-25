
# coding: utf-8

# # Matrix Addition
#
# In this exercises, you will write a function that accepts two matrices and
# outputs their sum.  Think about how you could do this with a for loop nested
# inside another for loop.

# In[ ]:


### TODO: Write a function called matrix_addition that
###     calculate the sum of two matrices
###
### INPUTS:
###    matrix A _ an m x n matrix
###    matrix B _ an m x n matrix
###
### OUPUT:
###   matrixSum _ sum of matrix A + matrix B
def matrix_addition(matrixA, matrixB):
    # initialize matrix to hold the results
    matrixSum = []
    
    # matrix to hold a row for appending sums of each element
    row = []
    
    # TODO: write a for loop within a for loop to iterate over
    # the matrices
    for m in range(len(matrixA)):
        for n in range(len(matrixA[m])):
            row.append(matrixA[m][n] + matrixB[m][n])
    # TODO: As you iterate through the matrices, add matching
    # elements and append the sum to the row variable
    
    # TODO: When a row is filled, append the row to matrixSum.
    # Then reinitialize row as an empty list
        matrixSum.append(row)
        row = []
    return matrixSum

### When you run this code cell, your matrix addition function
### will run on the A and B matrix.
A = [[2,5,1], 
    [6,9,7.4], 
    [2,1,1], 
    [8,5,3], 
    [2,1,6], 
    [5,3,1]]

B = [[7, 19, 5.1], 
    [6.5,9.2,7.4], 
    [2.8,1.5,12], 
    [8,5,3], 
    [2,1,6], 
    [2,33,1]]

matrix_addition(A, B)


# ### Vectors versus Matrices
#
# What happens if you run the cell below?  Here you are adding two vectors
# together.  Does your code still work?

# In[ ]:
#matrix_addition([4, 2, 1], [5, 2, 7])


# Why did this error occur?  Because your code assumes that a matrix is a
# two-dimensional grid represented by a list of lists.  But a horizontal
# vector, which can also be considered a matrix, is a one-dimensional grid
# represented by a single list.
#
# What happens if you store a vector as a list of lists like [[4, 2, 1]] and
# [[5, 2, 7]]?  Does your function work?  Run the code cell below to find out.

# In[ ]:
matrix_addition([[4, 2, 1]], [[5, 2, 7]])


# ### Test your Code
# Run the cell below.  If there is no output, then your results are as
# expected.

# In[ ]:
assert matrix_addition([[1, 2, 3]], 
    [[4, 5, 6]]) == [[5, 7, 9]]

assert matrix_addition([[4]], [[5]]) == [[9]]

assert matrix_addition([[1, 2, 3], 
                        [4, 5, 6]], 
                       [[7, 8, 9], 
                        [10, 11, 12]]) == [[8, 10, 12], 
                                           [14, 16, 18]]


