#!/usr/bin/env python
# coding: utf-8

# ## Conditional Statements

# In[1]:


#1.	 Take a variable ‘age’ which is of positive value and check the following:
#a.	If the age is less than 10, print “Children”.
#b.	If the age is more than 60, print ‘senior citizens’.
#c.	 If it is between 10 and 60, print ‘normal citizen’.


# In[3]:


age= int(input("enter your age: "))

if age<10:
    print("Childern")
elif age>60:
    print("Senior Citizens")
else:
    print("Normal Citizen")


# In[4]:


#2.	Find the final train ticket price with the following conditions. 
#a.	If male and ‘sr.citizen’, 70% of the fare is applicable
#b.	If female and ‘sr.citizen’, 50% of the fare is applicable.
#c.	If a female and a normal citizen, 70% of the fare is applicable.
#d.	If a male and a normal citizen, 100% of the fare is applicable.
#[Hint: First check for the gender, then calculate the fare based on the age factor. For both ‘Male’ and ‘Female’, consider them as sr.citizens if their age >=60]


# In[7]:


gender=input("Enter your Gender male/female: ")
age=int(input("Enter your age: "))
fee=100 # lets assume
def fare(gender,age):
    if gender== "male" and age<60:
        print("As a normal citizen you have to pay {} ".format(fee))
    elif gender== "male" and age>=60:
        print("As a sr.citizen you have to pay {} ".format(fee*70/100))
    elif gender== "female" and age<60:
        print("As a female citizen you have to pay {}".format(fee*70/100))
    else:
        print("As a female sr.citizen you have to pay {}".format(fee*50/100))
fare(gender,age)


# In[8]:


#3.	Check whether the given number is positive and divisible by 5 or not.  


# In[13]:


inputnumber=int(input("Enter a number: "))
if inputnumber>0:
    print("It is a positive number")
    if inputnumber%5==0:
        print("It is divisible by 5")
    else:
        print("It is not divisible by 5")
else:
    print("It is a negative number")
    if inputnumber%5==0:
        print("It is divisible by 5")
    else:
        print("It is not divisible by 5")


# ##  Conditional Statements
# 

# In[14]:


#1.	A) list1 = [1, 5.5, (10+20j), ’data science’]. Print default functions and parameters exist in list1.
#B) How do we create a sequence of numbers in Python?
#C) Read the input from the keyboard and print a sequence of numbers up to that number


# In[18]:


list1 = [1, 5.5, (10+20j), 'data science']
print(dir(list1))


# In[22]:


# we create a sequnce by using range
print(list(range(20)))


# In[23]:


i=int(input("Enter maximum limit of sequence: "))
print(list(range(i)))


# In[24]:


#2.	Create 2 lists: One list contains 10 numbers (list1 = [0, 1, 2, 3....9]) and another 
#list contains words of those 10 numbers (list2 = ['zero', 'one', 'two', ...., 'nine']).
#a.	Create a dictionary such that list2 are keys and list1 are values.


# In[26]:


list1=list(range(10))
list2=['zero','one','two','three','four','five','six','seven','eight','nine']
maps={}
for i in range(len(list1)):
    maps[list2[i]]=list1[i]


# In[28]:


print(maps)


# In[29]:


#3.	Consider list1 [3, 4, 5, 6, 7, 8]. 
#Create a new list2 such that Add 10 to the even number and multiply with 5 if it is an odd number in the list1.


# In[30]:


list1=[3,4,5,6,7,8]
list2=[]
for i in list1:
    if i%2==0:
        list2.append(i+10)
    else:
        list2.append(i*5)


# In[31]:


print(list2)


# In[32]:


#       4.     Write a simple user-defined function that greets a person in such a way that:
#i) It should accept both the name of a person and the message you want to deliver.
#ii) If no message is provided, it should greet a default message ‘How are you’.
          #	Ex: Hello ---xxxx---, How are you - default message.
           #	Ex: Hello ---xxxx---, --xx your message xx---


# In[37]:


def greeting(name,message): 
    print("Hello {},{}".format(name,message))
name=input("Enter your name: ")
message=input("Enter a message: ")
if message=="":
    message="How Are You?"
greeting(name,message)


# In[ ]:




