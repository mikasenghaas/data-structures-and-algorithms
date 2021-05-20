# convert any 10-base number into a binary number using stacks
from itu.algs4.fundamentals.stack import Stack
import sys


def convert_binary(n):
    stack = Stack()
    while n > 0:
        stack.push(n % 2)
        n //= 2
    string = ''
    for i in stack:
        string += str(i)
    return string


print(convert_binary(int(sys.argv[1])))
