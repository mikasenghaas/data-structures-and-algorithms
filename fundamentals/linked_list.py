# linked list implementation
from nodes import Node


class LinkedList:
    def __init__(self):
        self.front = self.back = None
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def add_to_back(self, item):
        temp = Node(item)

        if self.back == None:
            self.back = self.front = temp
            return

        self.back.next = temp
        self.back = temp
        self.n += 1

    def add_to_front(self, item):
        temp = Node(item)

        if self.back == None:
            self.back = self.front = temp
            return

        oldfront = self.front
        self.front = temp
        temp.next = oldfront
        self.n += 1

    def remove_from_front(self):
        item = self.front.item

        self.front = self.front.next
        self.n -= 1
        return item

    # only costly operation (that's why we choose the end of stack/queue to be different, since we want to remove from beginning)
    def remove_from_back(self):
        # O(n)
        curr = self.front
        while curr.next != self.back:
            curr = curr.next
        curr.next = None

    def find_max(self):
        _max = self.front.item
        curr = self.front
        while curr != None:
            if curr.item > _max:
                _max = curr.item
            curr = curr.next
        return _max

    def remove(self, item):
        if self.front.item == item:
            self.remove_from_front()
            self.n -= 1
        curr = self.front
        while curr != None:
            if curr.next.item == item:
                curr.next = curr.next.next
                self.n -= 1
            curr = curr.next

    def insert_at(self, item, i):
        insert = Node(item)

        if i == 0:
            self.add_to_front(item)
            return

        elif i > self.n:
            self.add_to_back(item)
            return

        x = 0
        curr = self.front
        while x < i-1:  # get left neighbor
            curr = curr.next
            x += 1
        next_one = curr.next
        curr.next = insert
        insert.next = next_one
        self.n += 1

    def __getitem__(self, i):
        x = 0
        curr = self.front
        while x < i:
            curr = curr.next
            x += 1
        return curr.item

    def __iter__(self):
        # iterate from front to back
        curr = self.front
        while curr != None:
            yield curr.item
            curr = curr.next

    def __str__(self):
        string = '[ '
        curr = self.front
        while curr != None:
            string += f'{curr.item} '
            curr = curr.next
        return string + ']'


if __name__ == '__main__':
    LL = LinkedList()
    for i in range(5):
        LL.add_to_front(i)
        LL.add_to_back(i)
    print(LL)
    LL.remove_from_back()
    LL.remove_from_front()
    print(LL)
