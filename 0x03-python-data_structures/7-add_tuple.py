#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    while (len(tuple_a) <2) or (len(tuple_b) < 2):
        if len(tuple_a) < 2:
            a = list(tuple_a)
            a.append(0)
         if len(tuple_b) < 2:
            b = list(tuple_b)
            a.append(0)

    i = a[0]+b[0]
    j = a[1]+b[1]
    return(i, j)