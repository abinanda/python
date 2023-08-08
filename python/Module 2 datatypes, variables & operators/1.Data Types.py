'''Data Types'''

## 1. Construct 2 lists containing all the available data types 
# (integer, float, string, complex and Boolean) and do the following.

# a. Create another list by concatenating above 2 lists.
# b. Find the frequency of each element in the concatenated list.
# c. Print the list in reverse order.
    

# 1. Construct 2 lists containing all the available data types 

list1 = [1, 3.14, "hello", 2+3j, True]
list2 = [42, 2.718, "world", 4-2j, False]


##### a. Create another list by concatenating above 2 lists

# using + operator to concat

list3 = list1 + list2

print("concatenated list for above two lists is:")

print(list3) # printing concatenated list3



##### b. Find the frequency of each element in the concatenated list.

frequency = {}

# iterating over the list

for item in list3:

  # checking the element in dictionary

  if item in frequency:

     # incrementing the count

     frequency[item] += 1

  else:

     # initializing the count

     frequency[item] = 1

# printing the frequency

print(" frequency of each element in the concatenated list.")

print(frequency)



##### c. Print the list in reverse order.

def Reverse(list3):

   new_lst3 = list3[::-1]

   return new_lst3

list3 = list1 + list2

print("list in reverse order is:")

print(Reverse(list3))



## 2. Create 2 Sets containing integers 
# (numbers from 1 to 10 in one set and 5 to 15 in other set)

# a. Find the common elements in above 2 Sets.
# b. Find the elements that are not common.
# c. Remove element 7 from both the Sets.


# 2. Create 2 Sets
set1 = set(range(1, 11))
set2 = set(range(5, 16))

##### a. Find the common elements in above 2 Sets. 

# To find the common elements in these sets, we can use the intersection() method:
common_elements = set1.intersection(set2)
print(common_elements)


##### b. Find the elements that are not common. 

not_common_elements = set1.symmetric_difference(set2)
print(not_common_elements)

##### c. Remove element 7 from both the Sets.

set1.discard(7)
print(set1)

set2.discard(7)
print(set2)



# 3. Create a data dictionary of 5 states having state name as key and number 
# of covid-19 cases as values.

# a. Print only state names from the dictionary.
# b. Update another country and it’s covid-19 cases in the dictionary.


# 3. Create a data dictionary
covid_cases = {
    'Andhra Pradesh': 2339312,
    'Arunachal Pradesh': 66891,
    'Assam': 746105,
    'Bihar': 851525,
    'Chandigarh': 99589
}


##### a. Print only state names from the dictionary. 

for state in covid_cases:
    print(state)

##### b. Update another country and it’s covid-19 cases in the dictionary.

covid_cases['India'] = 1234567
print(covid_cases)