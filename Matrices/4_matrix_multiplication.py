
# coding: utf-8

# # Matrix Multiplication
#
# Matrix multiplication involves quite a few steps in terms of writing code.
# But remember that the basics of matrix multiplicaiton involve taking a row in
# matrix A and finding the dot product with a column in matrix B.
#
# So you are going to write a function to extract a row from matrix A, extract
# a column from matrix B, and then calculate the dot product of the row and
# column.
#
# Then you can use these functions to output the results of multiplying two
# matrices together.
#
# Here is a general outline of the code that you will be writing.  Assume you
# are calculating the product of
#
# $$A\times{B}$$
#
# * Write a nested for loop that iterates through the m rows of matrix A and
# the p columns of matrix B
# * Initialize an empty list that will hold values of the final matrix
# * Starting with the first row of matrix A, find the dot product with the
# first column of matrix B
# * Append the result to the empty list representing a row in the final matrix
# * Now find the dot product between the first row of matrix A and the second
# column of matrix B
# * Append the result to the row list
# * Keep going until you get to the last column of B
# * Append the row list to the output variable.  Reinitialize the row list so
# that it is empty.
# * Then start on row two of matrix A.  Iterate through all of the columns of B
# taking the dot product
# * etc...

# # Breaking the Process down into steps
#
# Rather than writing all of the matrix multiplication code in one function,
# you are going to break the process down into several functions:
#
# **get_row(matrix, row_number)**
#
# Because you are going to need the rows from matrix A, you will use a function
# called get_row that takes in a matrix and row number and then returns a row
# of a matrix.  We have provided this function for you.
#
# **get_column(matrix, column_number)**
#
# Likewise, you will need the columns from matrix B.  So you will write a
# similar function that receives a matrix and column number and then returns a
# column from matrix B.
#
# **dot_product(vectorA, vectorB)**
#
# You have actually already written this function in a prevoius exercise.  The
# dot_product function calculates the dot product of two vectors.
#
# **matrix_multiply(matrixA, matrixB)**
#
# This is the function that will calculate the product of the two matrices.
# You will need to write a nested for loop that iterates through the rows of A
# and columns of B.  For each row-column combination, you will calculate the
# dot product and then append the result to the output matrix.

# # get_row
#
# The first function is the get_row function.  We have provided this function
# for you.
#
# The get_row function has two inputs and one output.
#
# INPUTS
# * matrix
# * row number
#
# OUTPUT
# * a list, which represents one row of the matrix
#
# In Python, a matrix is a list of lists.  If you have a matrix like this one:
# ```python
# m = [
#     [5, 9, 11, 2],
#     [3, 2, 99, 3],
#     [7, 1, 8, 2]
# ]
# ```
#
# then row one would be accessed by
# ```
# m[0]
# ```
#
# row two would be
# ```
# m[1]
# ```
#
# and row three would be
# ```
# m[2]
# ```

# In[ ]:


## TODO: Run this code cell to load the get_row function
## You do not need to modify this cell
def get_row(matrix, row):
    return matrix[row]


# # Getting a Column from a Matrix
#
# Since matrices are stored as lists of lists, it's relatively simple to
# extract a row.  If A is a matrix, then
# ```
# A[0]
# ```
#
# will output the first row of the matrix.
# ```
# A[1]
# ```
#
# outputs the second row of the matrix.
#
# But what if you want to get a matrix column?  It's not as convenient.  To get
# the values of the first column, you would need to output:
# ```
# A[0][0]
# A[1][0]
# A[2][0]
# ...
# A[m][0]
# ```
#
# For matrix multiplication, you will need to have access to the columns of the
# B matrix.  So write a function called get_column that receives a matrix and a
# column number indexed from zero.  The function then outputs a vector as a
# list that contains the column.  For example
# ```
# get_column([
#         [1, 2, 4],
#         [7, 8, 1],
#         [5, 2, 1]
#         ],
#     1)
# ```
#
# would output the second column
# ```
# [2, 8, 2]
# ```
#

# # get_column
#
# The get_column function is similar to the get_row function except now you
# will return a column.
#
# Here are the inputs and outputs of the function
#
# INPUTS
# * matrix
# * column number
#
# OUPUT
# * a list, which represents a column of the matrix
#
# Getting a matrix column is actually more difficult than getting a matrix row.
#
# Take a look again at this example matrix:
# ```python
# m = [
#     [5, 9, 11, 2],
#     [3, 2, 99, 3],
#     [7, 1, 8, 2]
# ]
# ```
#
# What if you wanted to extract the first column as a list [5, 3, 7].  You
# can't actually get that column directly like you could with a row.
#
# You'll need to think about using a for statement to iterate through the rows
# and grab the specific values that you want for your column list.
#

# In[ ]:


### TODO: Write a function that receives a matrix and a column number.
###       the output should be the column in the form of a list


### Example input:
# matrix = [
#    [5, 9, 11, 2],
#    [3, 2, 99, 3],
#    [7, 1, 8, 2]
# ]
#
# column_number = 1

### Example output:
# [9, 2, 1]
#
def get_column(matrix, column_number):
    column = []
    for row in matrix:
        column.append(row[column_number])
    return column


# In[ ]:


### TODO: Run this code to test your get_column function
assert get_column([[1, 2, 4], 
                   [7, 8, 1], 
                   [5, 2, 1]], 1) == [2, 8, 2]

assert get_column([[5]], 0) == [5]


# ### Dot Product of Two Vectors
#
# As part of calculating the product of a matrix, you need to do calculate the
# dot product of a row from matrix A with a column from matrix B.  You will do
# this process many times, so why not abstract the process into a function?
#
# If you consider a single row of A to be a vector and a single row of B to
# also be a vector, you can calculate the dot product.
#
# Remember that for matrix multiplication to be valid, A is size m x n while B
# is size n x p.  The number of columns in A must equal the number of rows in
# B, which makes taking the dot product between a row of A and column of B
# possible.
#
# As a reminder, the dot product of `<a1, a2, a3, a4>` and `<b1, b2, b3, b4>`
# is equal to
#
# `a1*b1 + a2*b2 + a3*b3 + a4*b4`
#

# In[ ]:


### TODO: Write a function called dot_product() that
###       has two vectors as inputs and outputs the dot product of the
###       two vectors.  First, you will need to do element-wise
###       multiplication and then sum the results.

### HINT: You wrote this function previously in the vector coding
###        exercises
def dot_product(vector_one, vector_two):    
    return sum(x[0] * x[1] for x in zip(vector_one, vector_two))


# In[ ]:


### TODO: Run this cell to test your results
assert dot_product([4, 5, 1], [2, 1, 5]) == 18
assert dot_product([6], [7]) == 42


# ### Matrix Multiplication
#
# Now you will write a function to carry out matrix multiplication
# between two matrices.
#
# If you have an m x n matrix and an n x p matrix, your result will be m x p.
#
# Your strategy could involve looping through an empty n x p matrix and filling
# in each elements value.

# In[ ]:


### TODO: Write a function called matrix_multiplication that takes
###       two matrices,multiplies them together and then returns
###       the results
###
###       Make sure that your function can handle matrices that contain
###       only one row or one column.  For example,
###       multiplying two matrices of size (4x1)x(1x4) should return a
###       4x4 matrix
def matrix_multiplication(matrixA, matrixB):
    
    ### TODO: store the number of rows in A and the number
    ###       of columns in B.  This will be the size of the output
    ###       matrix
    ### HINT: The len function in Python will be helpful
    m_rows = len(matrixA)
    n_columns = len(matrixA[0])

    n_rows = len(matrixB)
    p_columns = len(matrixB[0])
    
    
    # empty list that will hold the product of AxB
    result = []

    
    ### TODO: Write a for loop within a for loop.  The outside
    ###        for loop will iterate through m_rows.
    ###        The inside for loop will iterate through p_columns.
    for m in range(m_rows):
        temp_res = []
        for n in range(p_columns):
            column_vec = get_column(matrixB,n)
            row_vec = get_row(matrixA,m)
            temp_res.append(dot_product(row_vec,column_vec))
        result.append(temp_res)


    ### TODO: As you iterate through the m_rows and p_columns,
    ###        use your get_row function to grab the current A row
    ###        and use your get_column function to grab the current
    ###        B column.
    
    
    ### TODO: Calculate the dot product of the A row and the B column
    
    
    ### TODO: Append the dot product to an empty list called row_result.
    ###       This list will accumulate the values of a row
    ###        in the result matrix
    row_result = []
    
    ### TODO: After iterating through all of the columns in matrix B,
    ###       append the row_result list to the result variable.
    ###       Reinitialize the row_result to row_result = [].
    ###       Your for loop will move down to the next row
    ###       of matrix A.
    ###       The loop will iterate through all of the columns
    ###       taking the dot product
    ###       between the row in A and each column in B.
    
    ### TODO: return the result of AxB
    
    
    return result


# In[ ]:


### TODO: Run this code cell to test your results
assert matrix_multiplication([[5], [2]], [[5, 1]]) == [[25, 5], [10, 2]]
assert matrix_multiplication([[5, 1]], [[5], [2]]) == [[27]]
assert matrix_multiplication([[4]], [[3]]) == [[12]]
assert matrix_multiplication([[2, 1, 8, 2, 1], [5, 6, 4, 2, 1]], [[1, 7, 2], [2, 6, 3], [3, 1, 1], [1, 20, 1], [7, 4, 16]]) == [[37, 72, 33], [38, 119, 50]]


