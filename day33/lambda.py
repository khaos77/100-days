#main = lambda a, b, c: a + b - c
#print(main(7, 3, 5))

def myfunc(n):
  return lambda a : a * n
#a = 2

mydoubler = myfunc(2)

print(mydoubler(11))
#n = 11