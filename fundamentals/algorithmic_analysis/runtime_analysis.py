# example of some function in different input sizes n
import sys
from timeit import default_timer  # or use time command line argument instead

N = int(sys.argv[1])


def f(N):
    if N <= 2:
        return 1
    return f(N-1) + f(N-2)


print(f(6))
