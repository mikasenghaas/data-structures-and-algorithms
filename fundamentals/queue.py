# simple queue api in python (based on sedgewick and wayne, algs4 and itu.algs4 library)
from nodes import Node


class LinkedListQueue:
    def __init__(self):
        self.front = self.rear = None
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def see_front(self):
        if self.is_empty():
            raise ValueError('Stack Underflow')
        return self.front.item

    def see_rear(self):
        if self.is_empty():
            raise ValueError('Stack Underflow')
        return self.rear.item

    def enqueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
        self.n += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Stack Underflow')

        temp = self.front
        item = temp.item
        self.front = temp.next

        if(self.front == None):
            self.rear = None

        return item

    def __len__(self):
        return self.n

    def show(self):
        if self.is_empty():
            raise ValueError('Stack Underflow')
        print('[', end=' ')
        front = self.front
        while front is not None:
            print(front.item, end=' ')
            front = front.next
        print(']')

    def __str__(self):
        if self.is_empty():
            raise ValueError('Stack Underflow')
        string_representation = '['
        front = self.front
        while front is not None:
            string_representation += f' {str(front.item)}'
            front = front.next
        return string_representation + ' ]'

    def __iter__(self):
        if self.is_empty():
            raise ValueError('Stack Underflow')
        front = self.front
        while front != None:
            yield front.item
            front = front.next


class DynamicArrayQueue:
    def __init__(self):
        self.front = self.rear = self.n = 0
        self.queue = [None]*1

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def see_front(self):
        return self.queue[self.front]

    def see_rear(self):
        return self.queue[self.rear-1]

    def enqueue(self, item):
        self.queue[self.rear] = item
        self.rear += 1
        if self.rear == len(self.queue):
            self.rear = 0
        self.n += 1
        if self.n == len(self.queue):
            self.resize()

    def dequeue(self):
        out = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        if self.front == len(self.queue):
            self.front = 0
        self.n -= 1
        return out

    def resize(self):
        temp = [None] * (2*len(self.queue))
        for i in range(self.n):
            temp[i] = self.queue[(i + self.front) % len(self.queue)]
        self.queue = temp
        self.front = 0
        self.rear = self.n

    def __iter__(self):
        yielded = 0
        while yielded < self.n:
            yield self.queue[self.front]
            yielded += 1
            self.front += 1
            if self.front >= len(self.queue):
                self.front = 0

    def __str__(self):
        string = '[ '
        for i in range(len(self.queue)):
            string += f'{self.queue[i]} '
        return string + ']'


if __name__ == '__main__':
    queue1 = LinkedListQueue()
    queue2 = DynamicArrayQueue()

    for i in range(1, 10):
        queue1.enqueue(i)
        queue2.enqueue(i)
    queue1.dequeue()
    queue2.dequeue()

    for i in queue2:
        print(i)

    print(queue1)
    print(queue2)
    print("Queue Front " + str(queue1.see_front()))
    print("Queue Rear " + str(queue1.see_rear()))
    print("Queue Front " + str(queue2.see_front()))
    print("Queue Rear " + str(queue2.see_rear()))
