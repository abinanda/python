#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.	Construct 2 lists containing all the available data types (integer, float, string, complex and Boolean) and do the following.
#a.	Create another list by concatenating the above 2 lists.
#b.	Find the frequency of each element in the concatenated list.
#c.	Print the list in reverse order.


# In[6]:


list1 = [3,5.6,"abishek",2+3j,True]
list2 = [4,2.4,3,"360digitMG",7-5j,False]


# In[7]:


list3= list1 + list2
list3


# In[20]:


occurances= {}
for i in list3:
    occurances[i]= occurances.get(i,0)+1
occurances
    
    


# In[21]:



for i,n in occurances.items():
    print("The frequency of {} is {} times".format(i,n))


# In[28]:


list3.reverse()


# In[29]:


print(list3)


# In[30]:


#2.	Create 2 Sets containing integers (numbers from 1 to 10 in one set and 5 to 15 in another set)
#a.	Find the common elements in the above 2 Sets.
#b.	Find the elements that are not common.
#c.	Remove element 7 from both Sets.


# In[33]:


set1 = {1,4,2,5,6,7}
set2={2,4,5,6,3,7}
common= set1.intersection(set2)


# In[34]:


common


# In[50]:


uncommon= set1.symmetric_difference(set2)


# In[51]:


uncommon


# In[52]:


set1.discard(7)


# In[53]:


set2.discard(7)


# In[54]:


#3.	Create a data dictionary of 5 states having state name as key and number of covid-19 cases as values.
#a.	Print only state names from the dictionary.
#b.	Update another country and its covid-19 cases in the dictionary.


# In[55]:


covid_data={"tamilnadu":3526,"andrapradesh":3636,"kerala":1323,"karnataka":5374,"Telungana":5352}


# In[56]:


covid_data.keys()


# In[61]:


covid_data["maharashtra"]=4536


# In[62]:


covid_data


# In[63]:


#1.	A. Write an equation that relates   399, 543, and 12345.
#B.  “When I divide 5 by 3, I got 1. But when I divide -5 by 3, I got -2”—How would you justify it?


# In[64]:


result= 399*543-12345


# In[65]:


result


# In[66]:


#B.
# when it comes to floor division in  python 5//3 ...as the value is 1.6... but it rounds it to its floor value or lowest roundoff..so it result in 1
#as the lowest value moves towerds negative infinity...when  we do -5//3 it rounds it to -2 as -2 is lower than -1


# In[67]:


#       2.  a=5, b=3, c=10. What will be the output of the following:
          #    A. a/=b
           #   B. c*=5  


# In[70]:


#A. 
# a/=b == (a=a/b) so the output will be a=5.3 that equals 1.66..
#B.
#c*=5 == (c=c*5) so the output will be c=10*5 that equals 50


# In[71]:


#       3. A. How to check the presence of an alphabet ‘s’ in the word “Data Science”.
 #           B. How can you obtain 64 by using numbers 4 and 3.


# In[76]:


#A.
presence = "s" in "Data Science"


# In[73]:


presence  # since we checked for a lower case s it results in false 


# In[74]:


presence = "S" in "Data Science"


# In[75]:


presence


# In[77]:


#B.
result = 4**3


# In[78]:


result


# In[ ]:




