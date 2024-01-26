def select_second(l):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(l) < 2:
        return None
    else:
        return l[1]
    pass


lista = input().split()
print(select_second(lista))
