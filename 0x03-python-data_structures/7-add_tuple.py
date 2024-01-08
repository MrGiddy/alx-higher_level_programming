#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    def prepare_tuple(tup):
        if len(tup) == 0:
            return (0, 0)
        elif len(tup) == 1:
            return tup + (0,)
        elif len(tup) > 2:
            return tuple(tup[n] for n in range(2))
        else:
            return tup

    tuple_a = prepare_tuple(tuple_a)
    tuple_b = prepare_tuple(tuple_b)

    return tuple(sum(pair) for pair in zip(tuple_a, tuple_b))
