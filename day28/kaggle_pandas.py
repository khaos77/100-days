import pandas as pd
pd.set_option('display.max_rows', 5)
from learntools.core import binder; binder.bind(globals())
from learntools.pandas.creating_reading_and_writing import *
print("Setup complete.")
#1
# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame({'Apples': [30],'Bananas': [21]}, index=[0])
# Check your answer
q1.check()
fruits

#2
# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.
fruit_sales = pd.DataFrame({'Apples': [35, 41],'Bananas': [21,34]}, index=['2017 Sales', '2018 Sales'])
# Check your answer
q2.check()
fruit_sales

#3
ingredients = pd.Series(['4 cups', '1 cup', '2 large','1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')
# Check your answer
q3.check()
ingredients

#4
reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv", index_col = 0)
# Check your answer
q4.check()
reviews

#5
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals
