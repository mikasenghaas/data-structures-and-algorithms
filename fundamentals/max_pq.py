# simple max priority api in python (based on sedgewick and wayne, algs4 and itu.algs4 library)

class MaxPQ():
    """
    MaxPQ implementation using binary heaps.
    O(log(n)) Insertions and Remove Max Operations
    """

    def __init__(self, max_capacity=1):
        self.pq = [None]*(max_capacity + 1)
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def insert(self, item):
        # _resize if overflowing
        if self.n == len(self.pq) - 1:
            self._resize(2 * len(self.pq))

        self.n += 1  # increase element count
        self.pq[self.n] = item  # add element to bottom of heap
        self._swim(self.n)  # reheapify by swimming up

    def max(self):
        if self.is_empty():
            raise ValueError('No Elements in PQ')
        return self.pq[1]

    def del_max(self):
        _max = self.pq[1]
        self._exchange(self.pq, 1, self.n)  # _exchange with last element
        # print(self.pq)
        self.n -= 1
        # _sink down new root (which possibly violates heap order to its children)
        self._sink(1)
        # delete old max (that is now in last position of the heap)
        self.pq[self.n + 1] = None

        # halve array if quarter-full
        if self.n > 0 and self.n == (len(self.pq) - 1) // 4:
            self._resize(len(self.pq) // 2)

        return _max

    def _swim(self, k):
        # only _swim up if not already root and if parent is smaller
        while k > 1 and self._less(self.pq, k//2, k):
            self._exchange(self.pq, k//2, k)  # _exchange with parent
            k //= 2  # reset k to see if another _swim needs to be performed

    def _sink(self, k):
        while (2*k <= self.n):  # can only _sink if not leaf ( 2*index at root will also be > n )
            j = 2*k  # child
            # if left child smaller than right, move j to right
            if j < self.n and self._less(self.pq, j, j+1):
                j += 1
            # don't _sink if k (current node) is larger than its two children
            if self._less(self.pq, j, k):
                break
            self._exchange(self.pq, k, j)  # otherwise _exchange
            k = j  # reset k to potentially _sink further

    @staticmethod
    def _exchange(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def _less(arr, i, j):
        return arr[i] < arr[j]

    def _resize(self, capacity):
        temp = [None] * capacity
        for i in range(1, self.n + 1):
            temp[i] = self.pq[i]
        self.pq = temp

    def __len__(self):
        return self.n

    def __iter__(self):
        copy = MaxPQ(self.size())

        for i in range(1, self.n + 1):
            copy.insert(self.pq[i])
        for i in range(1, copy.n + 1):
            yield copy.del_max()

    def __str__(self):
        return str(self.pq)


if __name__ == '__main__':
    max_pq = MaxPQ()

    # for i in 'E A S Y Q U E S T I O N'.split():
    #    max_pq.insert(i)
    max_pq.insert(5)
    max_pq.insert(8)
    max_pq.insert(3)
    max_pq.del_max()
    max_pq.insert(9)
    max_pq.insert(2)
    max_pq.insert(4)
    print(max_pq)
    # print(max_pq.del_max())
    # print(max_pq.del_max())
