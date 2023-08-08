#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.	 Write a Python function to find the Max of three numbers.


# In[4]:


def maximumnum(anysequence):
    print(max(anysequence))
list1=[3,5,2]
maximumnum(list1)


# In[5]:


#2.	 Write a Python function to sum all the numbers in a list.


# In[6]:


def sumnum(anylist):
    a=0
    for i in anylist:
        a+=i
    print(a)
list2=[3,45,6,2,4,34]
sumnum(list2)


# In[7]:


#3.	 Write a Python function to multiply all the numbers in a list.


# In[8]:


def mult(anylist):
    a=1
    for i in anylist:
        a*=i
    print(a)
list3=[2,5,2,4,34,28,1,3.5]
mult(list3)


# In[ ]:




