
# coding: utf-8

# # Becoming "Wikipedia proficient"
#
# The goal of this course is **not** for you to memorize how to calculate a dot
# product or multiply matrices.  The goal is for you to be able to do something
# useful with a wikipedia page like their [article on Kalman
# Filters](https://en.wikipedia.org/wiki/Kalman_filter), even if requires some
# additional research and review from you.
#
# But these pages are usually written in the notation of **linear algebra** and
# not the notation of computer programming.
#
# In this notebook you will learn something about how to navigate the notation
# of linear algebra and how to translate it into computer code.

# ## Analyzing The Dot Product Equation
# At the time I'm writing this, the wikipedia article on the [dot
# product](https://en.wikipedia.org/wiki/Dot_product) begins with a section
# called **Algebraic Definition**, which starts like this:
#
# > The dot product of two vectors $\mathbf{a} = [a_1, a_2, \ldots, a_n]$ and
# $\mathbf{b} = [b_1, b_2, \ldots, b_n]$ is defined as:
# >
# > $$\mathbf{a} \cdot \mathbf{b} = \sum
# _{i=1}^{n}a_{i}b_{i}=a_{1}b_{1}+a_{2}b_{2}+\cdots +a_{n}b_{n}$$
#
# If you don't know what to look for, this can be pretty unhelfpul.  Let's take
# a look at three features of this equation which can be helpful to
# understand...
#
# ### Feature 1 - Lowercase vs uppercase variables
# This equation only uses lowercase variables.  In general, lowercase variables
# are used when discussing **vectors** or **scalars** (regular numbers like 3,
# -2.5, etc...) while UPPERCASE variables are reserved for matrices.
#
# ### Feature 2 - Bold vs regular typeface for variables
# A variable in **bold** typeface indicates a vector or a matrix.  A variable
# in regular typeface is a scalar.
#
#
# ### Feature 3 - "..." in equations
# When you see three dots $\ldots$ in an equation it means "this pattern could
# continue any number of times"
#
# #### EXAMPLE 1 - APPLYING FEATURES 1, 2, and 3
# When you see something like $\mathbf{a} = [a_1, a_2, \ldots, a_n]$ you can
# infer the following:
#
# 1.  **$\mathbf{a}$ is a vector**: since a is bold it's either a vector OR a
# matrix, but since it's also lowercase, we know it can only be a vector.
#
# 2.  **$\mathbf{a}$ can have any length**: since there's a $\ldots$ in the
# definition for $\mathbf{a}$, we know that in addition to $a_1$ and $a_2$
# there could also be $a_3$, $a_4$, and so on...
#
# 3.  **The values in the $\mathbf{a}$ vector are scalars**: since $a_1$ is
# lowercase and non-bold we know that it must be a scalar (regular number) as
# opposed to being a vector or matrix.

# ### Feature 4 - $\Sigma$ Notation
# The symbol $\Sigma$ is the uppercase version of the greek letter "sigma" and
# it is an instruction to perform a sum.
#
# **When you see a $\Sigma$ you should think "for loop!"**
#
# In the case of the dot product, the sigma instructs us to sum $a_ib_i$ for
# $i=1,2, \ldots, n$.  And in this case $n$ is just the length of the
# $\mathbf{a}$ and $\mathbf{b}$ vectors.
#
# How this for loop works is best explained with an example.  Take a look at
# the `dot_product` function defined below.  Try to read through the comments
# and really understand how the code connects to math.
#

# **The MATH**
#
# The dot product of two vectors $\mathbf{a} = [a_1, a_2, \ldots, a_n]$ and
# $\mathbf{b} = [b_1, b_2, \ldots, b_n]$ is defined as:
#
# $$\mathbf{a} \cdot \mathbf{b} = \sum
# _{i=1}^{n}a_{i}b_{i}=a_{1}b_{1}+a_{2}b_{2}+\cdots +a_{n}b_{n}$$

# In[4]:


# The CODE
def dot_product(a, b):
    # start by checking that a and b have the same length.
    # I know they SHOULD have the same length because they
    # each are DEFINED (in the first line above) to have n
    # elements.  Even though n isn't specified, the fact that
    # a goes from 0 to n AND b does the same (instead of going
    # from 0 to m for example) implies that these vectors
    # always should have the same length.
    if len(a) != len(b):
        print("Error! Vectors must have the same length!")
        return None
    
    # let's call the length of these vectors "n" so we can
    # be consistent with the mathematical notation
    n = len(a)
    
    # Since we want to add up a bunch of terms, we should
    # start by setting the total to zero and then add to
    # this total n times.
    total = 0
    
    # now we are going to perform the multiplication!
    # note that the algebraic version goes from 1 to n.
    # The Python version of this indexing will go from
    # 0 to n-1 (recall that range(3) returns [0,1,2] for example).
    for i in range(n): 
        a_i = a[i]
        b_i = b[i]
        total = total + a_i * b_i
        
    return total



# In[3]:


# let's see if it works
a = [3,2,4]
b = [2,5,9]

# a*b should be 3*2 + 2*5 + 4*9
# or...  6 + 10 + 36
#                            52
a_dot_b = dot_product(a,b)
print(a_dot_b)


