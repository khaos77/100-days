#questao 1
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    c = 0
    for num in nums:
        if num % 7 == 0:
            c += 1
    if c > 0:
        return True
    else:
        return False

#questao 2
def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    lis = []
    for i in L:
        if i > thresh:
            lis.append(True)

        else:
            lis.append(False)
    return lis
    pass
