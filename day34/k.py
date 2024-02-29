""""
a = lambda a: a + 1
print(a(372)) 

def func(a):
    return a + 1


print(func(372))
"""""

b = [2, 5, 8, 6, 9]
#for i in b:
#    print(i)
y = map(lambda x: x + 1, b)
#for i in y:
#    print(i)

print(b)
print(list(y))

trop = reviews.description.map(lambda d: 'tropical' in d).sum()
frut = reviews.description.map(lambda d: 'fruity' in d).sum()
descriptor_counts = pd.Series([trop, frut], index=['tropical', 'fruity'])