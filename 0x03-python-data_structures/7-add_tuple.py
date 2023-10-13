#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    for i in range(2):
        k = tuple_a[i] + tuple_b[i]
        new_tuple.append(k)
        l = tuple(new_tuple)
    return l


tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))