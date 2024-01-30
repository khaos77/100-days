def triangulo(n):
    for i in range(n + 1):
        a = n - i
        b = " * "*i
        print("-"*a + b + "-"*a)



triangulo(5)



