#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    answers = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
            answers.append(res)
        except ZeroDivisionError:
            print("division by 0")
            answers.append(0)
            continue
        except TypeError:
            print("wrong type")
            answers.append(0)
            continue
        except IndexError:
            print("out of range")
            answers.append(0)
            continue
        finally:
            pass
    return answers
