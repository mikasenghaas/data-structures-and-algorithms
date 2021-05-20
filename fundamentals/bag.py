# simple bag api in python (based on sedgewick and wayne, algs4 and itu.algs4 library)
from nodes import Node


class LinkedListBag:
    def __init__(self):
        self.first = None
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def add(self, item):
        oldfirst = self.first
        self.first = Node(item)
        self.first.next = oldfirst
        self.n += 1

    def show(self):
        print('{', end=' ')
        first = self.first
        while first != None:
            print(first.item, end=' ')
            first = first.next
        print('}')

    def __len__(self):
        return self.n

    def __str__(self):
        string_representation = '{'
        first = self.first
        while first != None:
            string_representation += f' {str(first.item)}'
            first = first.next
        return string_representation + ' }'

    def __iter__(self):
        first = self.first
        while first != None:
            yield first.item
            first = first.next


class DynamicArrayBag:
    def __init__(self):
        self.bag = [None]
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def add(self, item):
        if len(self.bag) == self.n:  # bag is full
            self.resize(2 * self.size())
        self.bag[self.n] = item
        self.n += 1

    def resize(self, capacity):
        temp = [None] * (2 * capacity)
        for i in range(self.n):
            temp[i] = self.bag[i]
        self.bag = temp

    def show(self):
        print('{ ', end='')
        for i in range(self.n):
            print(f'{self.bag[i]}', end=' ')
        print('}')

    def __len__(self):
        return self.n

    def __str__(self):
        string = '{ '
        for i in range(self.n):
            string += f'{self.bag[i]} '
        return string + '}'

    def __iter__(self):
        for i in range(self.n):
            yield self.bag[i]


if __name__ == '__main__':
    bag1 = LinkedListBag()
    bag2 = DynamicArrayBag()

    for i in range(1, 20, 2):
        bag1.add(i)
        bag2.add(i)

    print(bag1)
    print(bag2)
