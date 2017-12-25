
# coding: utf-8

# ## Coding Matrices
#
# Here are a few exercises to get you started with coding matrices.  The
# exercises start off with vectors and then get more challenging
#
# ### Vectors

# In[ ]:


### TODO: Assign the vector <5, 10, 2, 6, 1> to the variable v
v = [5,10,2,6,1]


# The v variable contains a Python list.  This list could also be thought of as
# a 1x5 matrix with 1 row and 5 columns.  How would you represent this list as
# a matrix?

# In[ ]:


### TODO: Assign the vector <5, 10, 2, 6, 1> to the variable mv
### The difference between a vector and a matrix in Python is that
### a matrix is a list of lists.

### Hint: See the last quiz on the previous page
mv = [[5,10,2,6,1]]


# How would you represent this vector in its vertical form with 5 rows and 1
# column?  When defining matrices in Python, each row is a list.  So in this
# case, you have 5 rows and thus will need 5 lists.
#
# As an example, this is what the vector $$<5, 7>$$ would look like as a 1x2
# matrix in Python:
# ```python
# matrix1by2 = [
#     [5, 7]
# ]
# ```
#
# And here is what the same vector would look like as a 2x1 matrix:
# ```python
# matrix2by1 = [
#     [5],
#     [7]
# ]
# ```

# In[ ]:


### TODO: Assign the vector <5, 10, 2, 6, 1> to the variable vT
### vT is a 5x1 matrix
vT = [[5],
      [10],
      [2],
      [6],
      [1]]


# ### Assigning Matrices to Variables

# In[ ]:


### TODO: Assign the following matrix to the variable m
### 8 7 1 2 3
### 1 5 2 9 0
### 8 2 2 4 1
m = [[8, 7, 1, 2, 3],
    [1, 5, 2, 9, 0],
     [8, 2, 2, 4, 1]]


# ### Accessing Matrix Values

# In[ ]:


### TODO: In matrix m, change the value
###       in the second row last column from 0 to 5
### Hint: You do not need to rewrite the entire matrix
m[1][4] = 5

# ### Looping through Matrices to do Math
#
# Coding mathematical operations with matrices can be tricky.  Because matrices
# are lists of lists, you will need to use a for loop inside another for loop.
# The outside for loop iterates over the rows and the inside for loop iterates
# over the columns.
#
#
# Here is some pseudo code
# ```python
# for i in number of rows:
#     for j in number of columns:
#          mymatrix[i][j]
# ```
#
# To figure out how many times to loop over the matrix, you need to know the
# number of rows and number of columns.
#
#
# If you have a variable with a matrix in it, how could you figure out the
# number of rows?  How could you figure out the number of columns?  The
# [len](https://docs.python.org/2/library/functions.html#len) function in
# Python might be helpful.

# ### Scalar Multiplication

# In[2]:


### TODO: Use for loops to multiply each matrix element by 5
###       Store the answer in the r variable.  This is called scalar
###       multiplication
###
### HINT: First write a for loop that iterates through the rows
###       one row at a time
###
###       Then write another for loop within the for loop that
###       iterates through the columns
###
###       If you used the variable i to represent rows and j
###       to represent columns, then m[i][j] would give you
###       access to each element in the matrix
###
###       Because r is an empty list, you cannot directly assign
###       a value like r[i][j] = m[i][j].  You might have to
###       work on one row at a time and then use r.append(row).
r = []
for ro in m:
    row = []
    for c in ro:
        row.append(c * 5)
    r.append(row)
# ### Printing Out a Matrix

# In[4]:


### TODO: Write a function called matrix_print()
###       that prints out a matrix in
###       a way that is easy to read.
###       Each element in a row should be separated by a tab
###       And each row should have its own line
###       You can test our your results with the m matrix

### HINT: You can use a for loop within a for loop
### In Python, the print() function will be useful
### print(5, '\t', end = '') will print out the integer 5,
###    then add a tab after the 5.  The end = '' makes sure that
###    the print function does not print out a new line if you do
###    not want a new line.

### Your output should look like this
### 8 7 1 2 3
### 1 5 2 9 5
### 8 2 2 4 1
def matrix_print(matrix):
    for r in matrix:
        for c in r:
            print(c, '\t', end = '')
        print('\n')
    return

m = [[8, 7, 1, 2, 3],
    [1, 5, 2, 9, 5],
    [8, 2, 2, 4, 1]]

matrix_print(m)


# ### Test Your Results

# In[ ]:


### You can run these tests to see if you have the expected
### results.  If everything is correct, this cell has no output
assert v == [5, 10, 2, 6, 1]
assert mv == [[5, 10, 2, 6, 1]]

assert vT == [[5], 
    [10], 
    [2], 
    [6], 
    [1]]

assert m == [[8, 7, 1, 2, 3], 
    [1, 5, 2, 9, 5], 
    [8, 2, 2, 4, 1]]

assert r == [[40, 35, 5, 10, 15], 
    [5, 25, 10, 45, 25], 
    [40, 10, 10, 20, 5]]


# ### Print Out Your Results

# In[ ]:


### Run this cell to print out your answers
print(v)
print(mv)
print(vT)
print(m)
print(r)


