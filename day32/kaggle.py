bargain_id = (reviews.points/reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_id, 'title']