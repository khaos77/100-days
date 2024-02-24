#1
median_points = reviews.points.median()
#2
countries = reviews.country.unique()
#3
reviews_per_country = reviews.country.value_counts()
#4
m = reviews.price.mean()
centered_price = reviews.price.map(lambda p: p - m)
#5

#6

#7