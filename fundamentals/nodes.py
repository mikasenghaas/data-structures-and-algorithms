# node represenation used throughout different algorithms (linked list, doubly linked list)

class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None

    def __repr__(self):
        return f'Item: {self.item}, Next: {self.next}'


class ThreeNode:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.previous = None

    def __repr__(self):
        return f'Item: {self.item}, Next: {self.next}, Previous: {self.previous}'
