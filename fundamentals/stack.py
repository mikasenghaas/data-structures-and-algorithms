# simple stack api in python (based on sedgewick and wayne, algs4 and itu.algs4 library)
from nodes import Node


class LinkedListStack:
    def __init__(self):
        self.top = None
        self.n = 0

    def push(self, item):
        oldtop = self.top
        self.top = Node(item)
        self.top.next = oldtop

        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack Underflow')
        item = self.top.item
        self.top = self.top.next
        self.n -= 1
        return item

    def is_empty(self):
        return self.n == 0

    def peek(self):
        if self.is_empty():
            raise ValueError('Stack Underflow')
        return self.top.item

    def length(self):
        return self.n

    def __len__(self):
        return self.n

    def show(self):
        if self.is_empty():
            raise ValueError('Stack Underflow')
        print('[', end=' ')
        top = self.top
        while top != None:
            print(top.item, end=' ')
            top = top.next
        print(']')

    def __str__(self):
        if self.is_empty():
            raise ValueError('Stack Underflow')
        string_representation = '['
        top = self.top
        while top != None:
            string_representation += f' {str(top.item)}'
            top = top.next
        return string_representation + ' ]'

    def __iter__(self):
        if self.is_empty():
            raise ValueError('Stack Underflow')
        top = self.top
        while top != None:
            yield top.item
            top = top.next


class DynamicArrayStack:
    def __init__(self):
        self.stack = [None]
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def peek(self):
        return self.stack[self.n-1]

    def push(self, item):
        if len(self.stack) == self.n:
            self.resize(2 * self.n)
        self.stack[self.n] = item
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack Underflow')
        self.n -= 1
        item = self.stack[self.n]
        self.stack[self.n] = None
        if self.n > 0 and self.n <= len(self.stack) // 4:
            self.resize(self.n // 2)

        return item

    def resize(self, capacity):
        temp = [None] * capacity
        for i in range(self.n):
            temp[i] = self.stack[i]
        self.stack = temp

    def __len__(self):
        return self.n

    def __str__(self):
        if self.is_empty():
            raise ValueError('Stack Underflow')
        string = '[ '
        for i in range(self.n-1, -1, -1):
            string += f'{self.stack[i]} '
        return string + ']'


if __name__ == '__main__':
    stack1 = LinkedListStack()
    stack2 = DynamicArrayStack()

    # it was - the best - of times - - - it was - the - -

    stack1.push('it')
    stack1.push('was')
    print(stack1.pop())
    stack1.push('the')
    stack1.push('best')
    print(stack1.pop())
    stack1.push('of')
    stack1.push('times')
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    stack1.push('it')
    stack1.push('was')
    print(stack1.pop())
    stack1.push('the')
    print(stack1.pop())
    print(stack1.pop())

    print(stack1)
