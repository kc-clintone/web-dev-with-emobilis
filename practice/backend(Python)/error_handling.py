import sys

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("An error occurred:", e, file=sys.stderr)
