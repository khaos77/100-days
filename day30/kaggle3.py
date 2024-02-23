#1
renamed = reviews.rename(columns={'region_1': 'region', 'region_2': 'locale'})
#2
reindexed = reviews.rename_axis('wines', axis= 'rows')
#3
combined_products = pd.concat([gaming_products, movie_products])
#4 - nao compreendi bem essa questao
left = powerlifting_meets.set_index(['MeetID'])
right = powerlifting_competitors.set_index(['MeetID'])

powerlifting_combined = left.join(right, lsuffix='_meet', rsuffix='_competitor')
powerlifting_combined.loc[0]