#!/usr/bin/python3

# if __name__ == "__main__":
#     """Print the sum of 1 and 2."""
#     from add_0 import add

#     a = 1
#     b = 2
#     print("{} + {} = {}".format(a, b, add(a, b)))

if __name__ == "__main__":
    """a function that imports from a module that adds the sum of 2 integers a and b"""
    from add_0 import add

    a = 1
    b = 2
    print(f"{a} + {b} = {add(a, b)}")