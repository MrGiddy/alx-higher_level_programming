#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple


def test_add_tuple():
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)
    
    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))

    # Test case 1: Both tuples are empty
    assert add_tuple() == (0, 0)

    # Test case 3: Both tuples have one element
    assert add_tuple((1,), (2,)) == (3, 0)

    # Test case 4: One tuple has more than two elements, the other is empty
    assert add_tuple((1, 2, 3), ()) == (1, 2)

    # Test case 5: One tuple has more than two elements, the other has one element
    assert add_tuple((1, 2, 3), (4,)) == (5, 2)

    # Test case 6: Both tuples have more than two elements
    assert add_tuple((1, 2, 3), (4, 5, 6)) == (5, 7)

    # Test case 7: Both tuples are the same length
    assert add_tuple((1, 2, 3), (4, 5, 6)) == (5, 7)

    print("All test cases passed!")

test_add_tuple()
