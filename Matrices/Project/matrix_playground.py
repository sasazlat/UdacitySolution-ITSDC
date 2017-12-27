
# coding: utf-8

# In[ ]:


# Run this cell but don't modify it.
#get_ipython().run_line_magic('load_ext', 'autoreload')
#get_ipython().run_line_magic('autoreload', '2')
from matrix import Matrix, zeroes, identity


# In[ ]:


# some functionality already exists...  here's a demo
m1 = Matrix([[1, 2],
    [3, 4]])

m2 = Matrix([[2, 5],
    [6, 1]])

print("m1 is")
print(m1)

print("m2 is")
print(m2)

print("we've also provided you with a function called zeros")
print("here's what happens when you call zeros(4,2)")
print(zeroes(4,2))

print("we've also provided you with a function called identity")
print("here's identity(3)")
print(identity(3))

print("but not everything works yet!")
print("for example, matrix addition...")
print("run the cell below to see what happens when we try...")


# In[ ]:

m1 = Matrix([
    [1, 2],
    [3, 4]
])

m2 = Matrix([
    [2, 5],
    [6, 1]
])

m3 = m1 + m2
print("m1 + m2 is")
print(m3)

m3 = m1 - m2
print("m1 - m2 is")
print(m3)

m3 = m1 * m2
print("m1 * m2 is")
print(m3)

neg = -m3
print("-m3 is")
print(neg)

m1 = Matrix([[1,2,3],
        [4,5,6]])

m2 = Matrix([[7,-2],
        [-3,-5],
        [4,1]])

m1_x_m2 = Matrix([[13,  -9],
        [37, -27]])

m2_x_m1 = Matrix([[-1,   4,   9],
        [-23, -31, -39],
        [8,  13,  18]])

m1_m2_inv = Matrix([[1.5, -0.5],
        [2.0555556, -0.722222222]])

m3 = m1 * m2
print("m1 * m2 is")
print(m3)

m3 = m2 * m1
print("m2 * m1 is")
print(m3)

neg = -m3
print("-m3 is")
print(neg)

m1_m2_inv1 = m1_x_m2.inverse()

# In[ ]:


# Try running this code.  You should get an assertion error.
# You will continue to get assertion errors until all the
# methods in matrix.py are correctly implemented.

# You can open matrix.py by selecting File > Open...
# and then selecting matrix.py
import test


# In[ ]:


# open matrix.py (File > Open...) and start
# implementing matrix methods! 

# when your code passes all the tests you can submit by 
# pressing the SUBMIT button in the lower right corner 
# of this page.


