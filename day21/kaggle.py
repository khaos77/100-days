#questao 1
def sign(x):
    if x < 0:
        return -1
    else:
        if x == 0:
            return 0
        else:
            return 1

n = int(input())
sign(n)