# MODULE – 3 ASSIGNMENT KEY

# Part I
### 1. Take a variable ‘age’ which is of positive value and check the following:
# a. If the age is less than 10, print “Children”.
# b. If the age is more than 60, print ‘senior citizens’.
# c. If it is between 10 and 60, print ‘normal citizen’.

age = int(input("age:"))
if age < 10: # if age is less than 10
    print("children")
elif age > 60:  # if age is greater than 60
    print("senior citizens")
else:
    print("normal citizens")



### 2. Find the final train ticket price with the following conditions. 
# a. If male and ‘sr.citizen’, 70% of the fare is applicable
# b. If female and ‘sr.citizen’, 50% of the fare is applicable.
# c. If a female and a normal citizen, 70% of the fare is applicable.
# d. If a male and a normal citizen, 100% of the fare is applicable.

# [Hint: First check for the gender, then calculate the fare based on the age factor.
# For both ‘Male’ and ‘Female’, consider them as sr.citizens if their age >=60]

age = int(input("age:"))
gender = input("gender:")
if age > 60 and gender == 'male':
    print("70% of fare is applicable")
elif age > 60 and gender == 'female':
    print("50% of fare is applicable")
elif (age > 10 and age < 60) and gender == 'female':
    print("70% of fare is applicable")
elif (age > 10 and age < 60) and gender == 'male':
    print("100% of fare is applicable")



### 3. Check whether the given number is positive and divisible by 5 or not.  

a = int(input("Enter the number:"))
if a > 0 and a % 5 == 0:
    print("number is positive and divisible by 5")
elif a < 0 and a % 5 == 0:
    print("number is negative and divisible by 5")
elif a > 0 and a % 5 != 0:
    print("number is postive and not divisible by 5")
elif a < 0 and a % 5 != 0:
    print("number is negative and not divisible by 5")


# Part II

# 1. A) list1 = [1, 5.5, (10+20j), ’data science’]. 
# Print default functions and parameters exist in list1.

list1 = [1, 5.5, complex(10, 20), 'data science']


# len() returns the number of items in the list
print(len(list1))  # Output: 4

# append() adds an item to the end of the list
list1.append(100)
print(list1)  # Output: [1, 5.5, (10+20j), 'data science', 100]

# remove() removes the first occurrence of an item from the list
list1.remove(5.5)
print(list1)  # Output: [1, (10+20j), 'data science', 100]

# index() returns the index of the first occurrence of an item in the list
print(list1.index('data science'))  # Output: 2

# count() returns the number of times an item appears in the list
print(list1.count(1))  # Output: 1



# B) How do we create a sequence of numbers in Python?

# Generate a sequence of numbers from 0 to 9
numbers = range(10)
print(list(numbers))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generate a sequence of even numbers from 0 to 10
even_numbers = range(0, 11, 2)
print(list(even_numbers))  # Output: [0, 2, 4, 6, 8, 10]



# C) Read the input from the keyboard and print a sequence of numbers up to that number
n = int(input("Enter a number: "))
numbers = range(1, n+1)
print(list(numbers))

	
	
### 2. Create 2 lists: One list contains 10 numbers (list1 = [0, 1, 2, 3....9]) 
# and another list contains words of those 10 numbers
# list2 = ['zero', 'one', 'two', ...., 'nine']).
# a. Create a dictionary such that list2 are keys and list1 are values.

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']	

dictionary = {}

for i in range(len(list1)):
    dictionary[list2[i]] = list1[i]

print(dictionary)


# 3. Consider a list1 [3, 4, 5, 6, 7, 8]. Create a new list2, 10 added to the
# even numbers, and multiply with 5 if the number is an odd number in the list1.

list1 = [3, 4, 5, 6, 7, 8]
list2 = []

for num in list1:
    if num % 2 == 0: # even number
        list2.append(num + 10)
    else: # odd number
        list2.append(num * 5)

print("Original list:", list1)
print("Modified list:", list2)
 

### 4. Write a simple user-defined function that greets a person in such a way that:
# i) It should accept both the name of a person and the message you want to deliver.
# ii) If no message is provided, it should greet a default message ‘How are you’.
          #	Ex: Hello ---xxxx---, How are you - default message.
          # Ex: Hello ---xxxx---, --xx your message xx---


def greet_person(name, message = 'How are you?'):
    print(f'Hello {name}, {message}')

# Example usage with only name argument
greet_person('John')
# Output: Hello John, How are you?

# Example usage with name and message arguments
greet_person('Jane', 'Nice to see you!')
# Output: Hello Jane, Nice to see you!

	