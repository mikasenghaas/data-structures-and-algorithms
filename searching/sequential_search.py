# sequential search symbol table/ dictionary in python (based on sedgewick and wayne, algs4 and itu.algs4 library)

class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None

    def __str__(self):
        return f'{self.key}, {self.val}, {self.next}'


class SequentialSearchDict:
    def __init__(self):
        self.first = None
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def get(self, key):
        if self.is_empty():
            return None

        curr = self.first
        while curr != None:
            if curr.key == key:
                return curr.val

            curr = curr.next
        return None

    def put(self, key, val):
        curr = self.first
        while curr != None:
            if curr.key == key:
                curr.val = val
                self.n += 1
                return
            curr = curr.next

        oldfirst = self.first
        self.first = Node(key, val)
        self.first.next = oldfirst
        self.n += 1

    def keys(self):
        curr = self.first
        while curr != None:
            yield curr.key
            curr = curr.next

    def values(self):
        curr = self.first
        while curr != None:
            yield curr.val
            curr = curr.next

    def __len__(self):
        return self.n

    def __iter__(self):
        curr = self.first
        while curr != None:
            yield curr.key
            curr = curr.next

    def __str__(self):
        string = '{'
        curr = self.first
        while curr != None:
            string += f'{curr.key} : {curr.val}, '
            curr = curr.next
        return string[:-2] + '}'


if __name__ == '__main__':
    dictionary = SequentialSearchDict()

    for i, char in enumerate('E A S Y Q U E S T I O N'.split()):
        dictionary.put(char, i)
    print(dictionary)
