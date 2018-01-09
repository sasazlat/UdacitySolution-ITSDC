
# coding: utf-8

# # Introduction to Sets
#
# A `set` in Python is a collection of **unique** and **immutable**
# (unchangeable) objects.
#
# To get a feel for how a set works, take a look at the following code:

# In[ ]:


# start with an empty set
my_set = set()

print(my_set)


# In[ ]:


# add a few elements
my_set.add('a')
my_set.add('b')
my_set.add('c')
my_set.add(1)
my_set.add(2)
my_set.add(3)

print(my_set)


# In[ ]:


# like a dictionary, a set is UNORDERED.
# We can still loop through a set though.
for element in my_set:
    print(element)


# In[ ]:


# let's see how many elements are in this set...
print("there are", len(my_set), "elements in my_set")


# In[ ]:


# can we make the set bigger by adding more "copies"
# of existing elements?
my_set.add("a")
my_set.add("a")
my_set.add("a")
my_set.add("a")
my_set.add("a")
my_set.add("a")
my_set.add("a")
my_set.add("a")

print("there are", len(my_set), "elements in my_set")


# In[ ]:


# there are still only 6 elements...
#
# that's because sets only care about UNIQUE elements.
# They do not allow for multiple "copies"
print(my_set)


# In[ ]:


# and they haven't changed.  What if we remove "a"
my_set.remove("a")
print("there are", len(my_set), "elements in my_set")
print(my_set)


# ### The Power of Sets
#
# The `set` is inspired by a branch of mathematics called [set
# theory](https://en.wikipedia.org/wiki/Set_theory).
#
# The thing that makes sets so useful is that they allow us to take advantage
# of "Venn Diagram logic".
#
# For example, consider two sets.  `primes`, which contains the prime numbers
# less than 10.  And `odds` which contains the odd numbers below 10.  A good
# way to think about the relationship between these sets is with a **Venn
# Diagram**

# ![Venn
# Diagram](https://d17h27t6h515a5.cloudfront.net/topher/2017/November/5a023c16_sets-1/sets-1.png)
#
# In this diagram, the blue area contains odds, the red contains primes, and
# the overlapping purple region contains numbers which are both odd and prime.

# ## Note - Go slow here!
#
# The next few cells demonstrate some of the **methods** that sets have.  As
# you read through them try to relate what each of these methods does to the
# Venn Diagram shown above.

# In[ ]:


# Initializing two sets
odds = set([1,3,5,7,9])
primes = set([2,3,5,7])


# In[ ]:


# Demonstration of the "intersection" between two sets
# The intersection corresponds to the overlapping region
# in the Venn Diagram above.
odd_AND_prime = odds.intersection(primes)
print(odd_AND_prime)


# In[ ]:


# Demonstration of the "union" of two sets.  The union
# of sets A and B includes ANY element that is in A OR B
# or both.
odd_OR_prime = odds.union(primes)
print(odd_OR_prime)


# In[ ]:


# Demonstration of the "set difference" between two sets.
# What do you expect odds-primes to return?
odd_not_prime = odds - primes
print(odd_not_prime)


# In[ ]:


# Another demo of "set difference"
prime_not_odd = primes - odds
print(prime_not_odd)


# ### Union vs Intersection
#
# The **union** of two sets A and B contains elements that are in A *or* B *or*
# both.  The **intersection** contains elements that are in both.
#
# ![set union vs
# intersection](https://d17h27t6h515a5.cloudfront.net/topher/2017/November/5a04a22f_sets-2/sets-2.png)

# ### `A-B` vs `B-A`
#
# **`A-B`** contains elements that are in A *but not* in B.
# **`B-A`** contains elements that are in B *but not* in A.
#
# ![set_a -
# set_b](https://d17h27t6h515a5.cloudfront.net/topher/2017/November/5a04a22f_sets-3/sets-3.png)
#
# ![set_b -
# set_a](https://d17h27t6h515a5.cloudfront.net/topher/2017/November/5a04a230_sets-4/sets-4.png)

# ## TODO - Exercise: A or B but not both
# Write a function that takes two sets (`set_a` and `set_b`) as input and
# returns a new set which contains elements that are either in `set_a` OR
# `set_b` but **not** in both.
#
# In the Venn Diagram above this would include everything in the diagram EXCEPT
# the overlapping middle area.  In this case that would be the numbers 9, 1,
# and 2
#
# NOTE - Try to use all of the following set operations in your answer:
#
# * **`intersection`**
# * **`union`**
# * **`difference`**

# In[ ]:
def a_or_b_but_not_both(set_a, set_b):
    """Returns a set which contains any element that is 
    a member of set_a OR a member of set_b but NOT a member
    of both."""

    return (set_a - (set_a.intersection(set_b))).union(set_b - (set_a.intersection(set_b)))

# testing code
assert a_or_b_but_not_both(odds, primes) == set([9,1,2])
print("Nice job! Your function works correctly!")


# In[ ]:


#

#

# Spoiler Alert!  Solution Below!

#

#

#

#

#

#

#

#

#

#


# In[ ]:


# Solution 1
def a_or_b_but_not_both(set_a, set_b):
    """Returns a set which contains any element that is 
    a member of set_a OR a member of set_b but NOT a member
    of both."""
    a_and_b = set_a.intersection(set_b)
    a_or_b = set_a.union(set_b)
    return a_or_b - a_and_b

assert a_or_b_but_not_both(odds, primes) == set([9,1,2])


# In[ ]:


# Solution 2
def a_or_b_but_not_both(set_a, set_b):
    """Returns a set which contains any element that is 
    a member of set_a OR a member of set_b but NOT a member
    of both."""
    a_without_b = set_a - set_b
    b_without_a = set_b - set_a
    return a_without_b.union(b_without_a)

assert a_or_b_but_not_both(odds, primes) == set([9,1,2])


# In[ ]:


# Solution 3
#
# There is actually a REALLY succinct way of writing this
# function using a single character.  I'm not going to tell
# you what that is now, but at the end of this notebook
# you'll find a link to Python documentation that will...


# ### Great, what about those tickets?  And labels?

# In[ ]:
def consolidate_labels(t1_labels, t2_labels):
    """
    Combines labels from two tickets without duplication.
    
    Given t1_labels and t2_labels (both lists), return 
    a consolidated list of labels without duplicates.
    """
    
    # TODO - rewrite this function to use sets.  You should
    #   be able to replace all the code below with 1 or 2
    #   lines if you use sets appropriately.
    #
    # NOTE - to convert a set back to a list, you can
    #   use the list() function (demonstrated in the
    #   cell below).
    
    combined = []
    combined = list(set(t1_labels).union(set(t2_labels)))
    return combined


# testing code
labels_1 = ["python", "bug", "localization", "bug"]
labels_2 = ["planning", "localization"]

combined_labels = consolidate_labels(labels_1, labels_2)

assert(set(combined_labels) == set(["python", "bug", 
                                     "localization", "planning"]))
# In[ ]:

## ### Additional set notation!
## 
## Now that you're getting more familiar with a variety of data structures, it's important to learn how to work with the documentation that describes these data structures.
## 
## Check out the [Python documentation on sets](https://docs.python.org/3/tutorial/datastructures.html#sets) and see if you can find an operator that solves the 
## "a_or_b_but_not_both"problem from earlier...

