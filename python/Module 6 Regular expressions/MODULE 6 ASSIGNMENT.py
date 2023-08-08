#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1)	Write a Python program to check that a string contains only a certain set of characters.
#(In this case a-z, A-Z, and 0-9).      


# In[9]:


import re
text1="hgdvwyvdabGVSVWHGV6546866"
pattern=r"^[a-zA-Z0-9]+$"
matches=re.findall(pattern,text1)
if matches:
    print(matches ,"yes it does have only these set of characters")
else:
    print("no it doesn't have only these set of characters")


# In[10]:


import re
text1="hgdvwyvdabGVSVWHGV//6546866"
pattern=r"^[a-zA-Z0-9]+$"
matches=re.findall(pattern,text1)
if matches:
    print(matches ,"yes it does have only these set of characters")
else:
    print("no it doesn't have only these set of characters")


# In[11]:


# 2)	Write a Python program to replace all occurrences of space, commas, or dots with a colon.


# In[12]:


text2="jbdbdqd qjqdwj,,dkbqdbb..wd."
text2=re.sub(r"[\s,\.]",":",text2)
print(text2)


# In[ ]:




