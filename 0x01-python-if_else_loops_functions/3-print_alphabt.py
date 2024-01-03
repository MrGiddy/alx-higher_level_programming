#!/usr/bin/python3

for _ in range(ord('a'), ord('z') + 1):
    if (_ == ord('q') or _ == ord('e')):
        continue
    else:
        print("{}".format(chr(_)), end="")
