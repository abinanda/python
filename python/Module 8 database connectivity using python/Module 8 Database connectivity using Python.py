# Module 8 Database Conectivity

### 1) Connect to MySQL using Python, and push "Data.csv" into the database.

# import libraries
import pandas as pd
# Import data (.csv file) using pandas.
data = pd.read_csv("Data.csv")
 

# - SQLAlchemy is basically referred to as the toolkit of Python SQL that 
# provides developers with the flexibility of using the SQL database. 
# - The benefit of using this particular library is to allow Python developers 
# to work with the language's own objects, and not write separate SQL queries.

# pip install sqlalchemy
from sqlalchemy import create_engine
from urllib.parse import quote

# **Engine Configuration**
# The Engine is the starting point for any SQLAlchemy application. 
# It’s “home base” for the actual database and its DBAPI delivered to the 
# SQLAlchemy application through a connection pool and a Dialect, which 
# describes how to talk to a specific kind of database/DBAPI combination.
# sqlalchemy helps to connect mysql, postgresql, microsoftsql(mssql), etc;

# Refer to url for brief Knowledge about "create_engine"
# https://docs.sqlalchemy.org/en/20/core/engines.html

## For mysql
# pip install pymysql
user = "root",# user
pw = "dba123", # passwrd
db = "databasename" #database

engine = create_engine("mysql+pymysql://{user}:%s@localhost/{db}" % quote(f'{pw}'))
                       

# To send data into DataBase
# DataFrame.to_sql(name, con, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None, method=None)

# Go to this link for more details
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
# Databases supported by SQLAlchemy are supported. Tables can be newly created,
# appended to, or overwritten.

data.to_sql('data', con = engine, if_exists = 'replace', chunksize = None, index = False) 
# sending data into database and connecting with Engine by using "DataFrame.to_sql()"



### 2) Connect to MySQL using Python, push "Indian Cities.csv" into the database,
# and then use Python to load the data from MySQL.

# import libraries
import pandas as pd
# Import data (.csv file) using pandas.
cities = pd.read_csv("Indian Cities.csv")

from sqlalchemy import create_engine
from urllib.parse import quote

user = "root",# user
pw = "dba123", # passwrd
db = "databasename" #database

engine = create_engine("mysql+pymysql://{user}:%s@localhost/{db}" % quote(f'{pw}'))
                       
data.to_sql('cities', con = engine, if_exists = 'replace', chunksize = None, index = False) 


# To get the data From DataBase
sql = "SELECT * FROM cities;" # write a query of sql 
Ind_cities = pd.read_sql_query(sql, engine) 
# connecting query with Engine and reading the results by using "pd.read_sql_query"
