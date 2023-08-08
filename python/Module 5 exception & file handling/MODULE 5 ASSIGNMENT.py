#!/usr/bin/env python
# coding: utf-8

# ### 1) Write the code in Python to open a file named “try.txt”

# In[7]:


text="""If an exception occurs within the try block, the execution jumps to the appropriate except block based on the type of exception.
In this case, if a ZeroDivisionError occurs (division by 0), the code inside the except block for ZeroDivisionError is executed, which prints the error message.
Since there is no other except block for other types of ex"""

file=open("try.txt",'w+')
file.write(text)
file.close()


# In[9]:


with open ("try.txt") as file:
    x=file.read()
    print(x)


# ### 2) What is the purpose of ‘r’ as a prefix in the given statement? 
#      #f = open(r, “d:\color\flower.txt”)
# 

#  in python \ slash is used an escape statement for a charavter in a string.. 
# for avoiding python form assuming the slash \ used in the document path...we are using r as prefix
#  it will limit python from assuming the slash as an escape statement

# ### 3) Write a note on the following
# #A.	Purpose of Exception Handling
# #B.	Try block
# #C.	Except block
# #D.	Else block
# #E.	Finally block
# #F.	Bulit-in exceptions
# 

# A. Purpose of exception handling: Exception handling used to avoid the runtime errors occurs when a condition or a statements or a function etc fails. it is used to avoid program crashing
#  
# B. TRY BLOCK : Try block will ec=xecute the block of code that is given inside the try block first and it pushes to the next step of program skipping except ...if the code in try block works correctly
# 
# C. Except Block : Except block will raise an error that we defined to raise if the code in try block doesnt function properly..or the code inside the except block will be executed
# 
# D. ELSE BLOCK : Else block will execute the code in it ...if the previous block try works properly and an exceptiomn is not raised
# 
# E. FINALLY BLOCK : Finally block will execute the code in it...no matter the previous blocks executed properly or raised an exception
# 

# In[14]:


# F. BULIT in EXCEPTIONS
print(dir(locals()['__builtins__']))


# ### 4) Write 2 Custom exceptions

# In[21]:


try:
    x = int(input("Enter a number: "))
    if x < 0:
        raise ValueError("CustomException1: Number must be positive")

except ValueError as e:
    print(e)


# In[22]:


try:
    x = int(input("Enter a number: "))
    assert x % 2 == 0, "CustomException2: Number must be even"
except AssertionError as e:
    print(e)


# In[ ]:




