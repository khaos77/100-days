a = int(input())
b= int(input())
c = int(input())

if a == b and b == c:
    print("equilatero")

else:
    if a != b and b != c and a != c:
        print("escaleno")
    else:
        print("isosceles")