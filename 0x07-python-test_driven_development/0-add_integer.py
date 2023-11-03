def add_integer(a, b=98):
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")
    else:
        return a + b
    
b = add_integer(1, 2)
print(b)