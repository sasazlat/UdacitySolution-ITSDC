
# coding: utf-8

# # The problems with strings and lists...
# In this notebook you will run into some problems when we try to represent tickets first with strings and then with lists. 
# 
# ## What data do we need to track?
# For now a single `ticket` needs to have three pieces of data associated with it:
# 
# * A date. For example `"2018-12-31"`.
# 
# * A priority. Either `"high"`, `"medium"`, or `"low"`.
# 
# * A description.
# 
# ### Attempt 1 - Represent a ticket as a string

# In[1]:


# Option 1 - represent a ticket as a string where each 
# field is separated by a newline \n character.
def create_ticket(date, priority, description):
    ticket = date + "\n"
    ticket = ticket + priority + "\n"
    ticket = ticket + description + "\n"
    return ticket


# In[2]:


ticket_1 = create_ticket("2018-12-31", "low", "example description")


# In[3]:


print(ticket_1)


# In[ ]:


# let's see how easy it is to do a common task using this
# string representation of a ticket. The following function
# retrieves a "description" from a ticket.
def get_description(ticket):
    
    # 1. separate string into individual lines
    lines = ticket.splitlines()
    
    # 2. get the last line (which has the description)
    description = lines[-1]
    
    return description


# In[ ]:


description_1 = get_description(ticket_1)
print(description_1)


# ### It seems to work... right?
# So far, it seems like strings work just fine. But it doesn't take much of an "edge case" to break this system...

# In[ ]:


date = "2018-12-29"
priority = "high"
description = """Vehicle did not slow down when 
SLOW
SCHOOL
ZONE
was written on road."""

ticket_2 = create_ticket(date, priority, description)


# In[ ]:


# what do you think will happen when we try to retrieve a
# description from this ticket using our get_description function?
description_2 = get_description(ticket_2)
print(description_2)


# ### Let's fix it! Right?
# 
# Sure... you could fix this particular problem with a clever `get_description` function. But this would require more code, it would be harder to read and it wouldn't address the root problem here:
# 
# > **A string is not the right data structure to represent a ticket**. Even though a ticket is just a bunch of text, that text has *structure* and representing a ticket with a string ignores that structure.
# 
# ---------
# 
# ## Attempt 2 - Represent a ticket as a list
# The code below is significantly more concise than the code for a string-representation of a ticket. It's also more robust to certain problems.

# In[ ]:


# Option 2 - Use a list to represent a ticket
def create_ticket(date, priority, description):
    return [date, priority, description]

def get_description(ticket):
    return ticket[-1]

date = "2018-12-29"
priority = "high"
description = """Vehicle did not slow down when 
SLOW
SCHOOL
ZONE
was written on road."""

ticket_2 = create_ticket(date, priority, description)


# In[ ]:


# what do you think will happen when we try to retrieve a
# description from this ticket using our NEW get_description function?
description_2 = get_description(ticket_2)
print(description_2)


# ### So what's the problem?
# This list is **not** a bad choice when a ticket just has these three fields. But for readability reasons wouldn't it be nice if we could write code like this:
# 
# ```python
# priority =    ticket['priority']
# date =        ticket['date']
# description = ticket['description']
# ```
# 
# instead of code like this:
# 
# ```python
# priority =    ticket[1]
# date =        ticket[0]
# description = ticket[2]
# ```
# 
# there are other reasons why lists aren't optimal (which you will explore later), but let's focus on the readability improvements for now.
# 
# In the next section you'll learn more about the python `dictionary`. Here's a peek at how they work:

# In[ ]:


dictionary_ticket = {"date" : "2018-12-28",
                     "priority" : "low",
                     "description" : "car drove too slow"}


# In[ ]:


print(dictionary_ticket['description'])


