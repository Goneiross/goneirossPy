def createList(value, n):
    """
    @param value: value to initialize the list
    @param n: list size to be created
    @return: size n list initialized to value
    """
    return [value for i in range (n)]

def merge(a, b):
    """
    @param a: a list
    @param b: a list
    @return: a and b list merged
    """
    return list(a) + list (b)