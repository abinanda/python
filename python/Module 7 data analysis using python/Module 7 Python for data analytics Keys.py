# Module 7 Python for data analytics Assignment Keys

### 1) Please take care of missing data present in the “Data.csv” file using 
# the Python module “sklearn.impute” and its methods, also collect all the 
# data that has “Salary” less than “70,000”.

import pandas as pd
from sklearn.impute import SimpleImputer

# Load data from CSV file
df = pd.read_csv('Data.csv')
df

# Check for missing data
print(df.isnull().sum())

# Impute missing data using SimpleImputer
imputer = SimpleImputer(strategy='mean')
df[['age', 'Salaries']] = imputer.fit_transform(df[['age', 'Salaries']])

# Collect all data with salary less than 70,000
low_salary_data = df[df['Salaries'] < 70000]

# Print the results
print("Data with missing values imputed:")
print(df)
print("Data with salary less than 70,000:")
print(low_salary_data)



### 2) Subtracting dates
'''
Python date objects let us treat calendar dates as something similar to 
numbers: we can compare them, sort them, add, and even subtract them.
Do math with dates in a way that would be a pain to do by hand. The 2007 
Florida hurricane season was one of the busiest on record, with 8 hurricanes
in one year. The first one hit on May 9th, 2007, and the last one hit on 
December 13th, 2007. How many days elapsed between the first and last 
hurricane in 2007?
Instructions:
 Import date from datetime.
 Create a date object for May 9th, 2007, and assign it to the start variable.
 Create a date object for December 13th, 2007, and assign it to the end variable.
 Subtract start from end, to print the number of days in the resulting timedelta object.
'''


from datetime import date

# Create date object for May 9th, 2007
start = date(2007, 5, 9)

# Create date object for December 13th, 2007
end = date(2007, 12, 13)

# Subtract start from end to get timedelta object
elapsed_time = end - start

# Print the number of days in the timedelta object
print("Number of days elapsed between the first and last hurricane in 2007:", elapsed_time.days)



### 3) Representing dates in different ways
'''
Date objects in Python have a great number of ways they can be printed out as 
strings. In some cases, you want to know the date in a clear, language-agnostic
format. In other cases, you want something which can fit into a paragraph and
flow naturally.
Print out the same date, August 26, 1992 (the day that Hurricane Andrew made 
landfall in Florida), in a number of different ways, by using the
 “ .strftime() ” method. Store it in a variable called “Andrew”.
'''

# Instructions: 	
# Print it in the format 'YYYY-MM', 'YYYY-DDD' and 'MONTH (YYYY)'

from datetime import date

# Create a date object for August 26, 1992
Andrew = date(1992, 8, 26)

# Print the date in the format 'YYYY-MM'
print(Andrew.strftime('%Y-%m'))

# Print the date in the format 'YYYY-DDD'
print(Andrew.strftime('%Y-%j'))

# Print the date in the format 'MONTH (YYYY)'
print(Andrew.strftime('%B (%Y)'))



### 4) For the dataset “Indian_cities”:

# a. Find out top 10 states in female-male sex ratio
# b. Find out top 10 cities in total number of graduates
# c. Find out top 10 cities and their locations in respect of total effective_literacy_rate.


# Import the dataset
import pandas as pd

indian_cities = pd.read_csv("Indian_cities.csv")
indian_cities.head()

## a) Find out top 10 states with female-male sex ratio
gp_s = indian_cities.groupby('state_name').sum()   # Group the data based on state
gp_s       
st = gp_s[['sex_ratio']].sort_values('sex_ratio', ascending = False) # After grouping the states we check by sorting the values of the column sex ratio in descending order.
st.head(10)  # print the top 10 states

## b) Find out top 10 cities with total number of graduates
gp_c = indian_cities.groupby('name_of_city').sum()
gp_c.head()
city = gp_c[['total_graduates']].sort_values('total_graduates', ascending = False)
city.head(10)

## c) Find out top 10 cities and their locations with respect to total effective_literacy_rate
# Using nlargest function we get the top 10 records and then specify the column we want to print.
indian_cities.nlargest(10, ['effective_literacy_rate_total'])[['name_of_city','location']]


### 5) For the data set “Indian_cities”
# a. Construct histogram on literates_total and comment about the inferences
# b. Construct scatter  plot between  male graduates and female graduates


## a. Construct histogram on literates_total and comment about the inferences
import matplotlib.pyplot as plt
plt.hist(indian_cities.literates_total)
plt.plot()

'''Inferences from histogram:
#	The data represented on the histogram is not symmetrical.
#	It has a long positive tail. It has a positive skewness.
#	More than 90% of the data is confined in the range 56998 to 416998.
#	Outliers are present in the dataset.
'''

## b) Construct scatter plot between male graduates and female graduates

# Using matplotlib.pyplot library we create the scatter plot.
# x = indian_cities.male_graduates
# y = indian_cities.female_graduates
plt.scatter(indian_cities.male_graduates, indian_cities.female_graduates, edgecolors = ('red'))
plt.plot()



### 6) For the data set “Indian_cities”
# a. Construct Boxplot on total effective literacy rate and draw inferences.
# b  Find out the number of null values in each column of the dataset and delete them.


## a) Construct Boxplot on total effective literacy rate and draw inferences
import matplotlib.pyplot as plt # Import the library to create visualizations
plt.boxplot(indian_cities.effective_literacy_rate_total)
plt.plot()
'''
# Inferences from boxplot:
#	The data represented on the boxplot is not symmetrical.
#	It has negative skewness as the median of the data is close to the upper end of the boxplot.
#	Outliers are present in the dataset beyond the lower whisker.
#	The median of the data is approximately 85.
#	The spread of the data is not much and majority of the data is confined between the range 80% to 90%.
'''


## b) Find out the number of null values in each column of the dataset and delete them


indian_cities.isnull().sum() # There are no missing values in the dataset.

### if in case there was a null values
# indian_cities = indian_cities.dropna(axis = 0, inplace = True) 
