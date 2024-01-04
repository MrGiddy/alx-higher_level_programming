#!/usr/bin/python3
import hidden_4


def print_hidden_discovery():
    names_list = []

    for name in dir(hidden_4):
        if name.startswith("__"):
            continue
        else:
            names_list.append(name)

    for name in sorted(names_list):
        print(name)


if __name__ == "__main__":
    print_hidden_discovery()
