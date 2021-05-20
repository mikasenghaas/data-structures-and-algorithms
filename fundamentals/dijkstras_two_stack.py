# python implementation of dijkstra's two-stack algorithm for evaluating arithmetic expressions
from itu.algs4.fundamentals.stack import Stack


def evaluate(expression):
    ops = Stack()
    vals = Stack()

    for char in expression:
        if char == '(':
            None
        elif char == '+':
            ops.push('+')
        elif char == '-':
            ops.push('-')
        elif char == '*':
            ops.push('*')
        elif char == '/':
            ops.push('/')
        elif char == ')':
            op = ops.pop()
            v = vals.pop()

            if op == '+':
                v = vals.pop() + v
            elif op == '-':
                v = vals.pop() - v
            elif op == '*':
                v = vals.pop() * v
            elif op == '/':
                v = vals.pop() / v
            vals.push(v)
        else:
            vals.push(int(char))
        #print(f'Operation Stack: {ops}')
        #print(f'Value Stack: {vals}')

    return vals.pop()


if __name__ == '__main__':
    print(evaluate('(1+2+2)'))
