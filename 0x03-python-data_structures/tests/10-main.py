#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

def test_divisible_by_2():

    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)

    i = 0
    while i < len(list_result):
        print("{:} {:s} is divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
        i += 1

    # Test case 1: Empty list
    assert divisible_by_2([]) == []

    # Test case 2: List with even numbers
    assert divisible_by_2([2, 4, 6, 8, 10]) == [True, True, True, True, True]

    # Test case 3: List with odd numbers
    assert divisible_by_2([1, 3, 5, 7, 9]) == [False, False, False, False, False]

    # Test case 4: List with a mix of even and odd numbers
    assert divisible_by_2([2, 3, 4, 5, 6]) == [True, False, True, False, True]

    # Test case 5: List with negative even numbers
    assert divisible_by_2([-2, -4, -6, -8, -10]) == [True, True, True, True, True]

    # Test case 6: List with negative odd numbers
    assert divisible_by_2([-1, -3, -5, -7, -9]) == [False, False, False, False, False]

    # Test case 7: List with a mix of negative even and odd numbers
    assert divisible_by_2([-2, -3, -4, -5, -6]) == [True, False, True, False, True]

    # Test case 8: List with zero
    assert divisible_by_2([0]) == [True]

    print("All test cases passed!")

# Run the test cases
test_divisible_by_2()
