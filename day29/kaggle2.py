import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.indexing_selecting_and_assigning import *
print("Setup complete.")
#1
desc = reviews.description
#2
first_description = reviews['description'][0]
#3
first_row = reviews.iloc[0]
#4
first_descriptions = reviews.loc[0:9, 'description']
#5
sample_reviews = reviews.iloc[[1,2,3,5,8], :]
#6
df = reviews.iloc[[0,1, 10, 100], [0, 5, 6, 7]]
#7
df = reviews.iloc[0:100,[0,11]]
#8
italian_wines = reviews.loc[reviews.country == 'Italy']
#9
top_oceania_wines = reviews.loc[((reviews.country == 'Australia')|(reviews.country == 'New Zealand')) & (reviews.points >= 95)]
