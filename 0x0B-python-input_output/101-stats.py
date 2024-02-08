#!/usr/bin/python3
""" Defines a script that reads stdin line by line and computes metrics """


def print_metrics(size, status_codes):
    """ Prints computed metrics """
    print(f'File size: {size}')
    for code in sorted(status_codes):
        print(f'{code}: {status_codes[code]}')


if __name__ == "__main__":
    import sys

    status_codes = {}
    size = 0
    lines_processed = 0
    true_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    try:
        for line in sys.stdin:
            line = line.rstrip().split()

            try:
                size += int(line[-1])
                if int(line[-2]) in true_codes:
                    status_codes[line[-2]] = status_codes.get(line[-2], 0) + 1
                lines_processed += 1
            except (IndexError, ValueError):
                pass

            if lines_processed == 10:
                print_metrics(size, status_codes)
                lines_processed = 0
    except KeyboardInterrupt:
        print_metrics(size, status_codes)
        raise
