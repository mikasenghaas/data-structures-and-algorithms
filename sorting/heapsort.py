# heapsort api in python (based on sedgewick and wayne, algs4 and itu.algs4 library)

class HeapSort():
    """
    Implementation of Heap Sort in Ascending Order

    Analysis:
    """

    def __init__(self, arr):
        self.arr = [None] + arr  # initialise array to store binary heap
        self.n = len(arr)  # number of elements in data structures

    def sort(self):
        # heap construction
        # sink down first half of array (excluding None type at index 0)
        for k in range(self.n // 2, 0, -1):
            self._sink(k)

        # sorting down using sink
        # iterate over n-1 elements in array (last one doesn't need to be examined, since must be at right position)
        while self.n > 1:
            # exchange root (highest key) with bottom node (max at last (final) position)
            self._exchange(self.arr, 1, self.n)
            self.n -= 1  # decrease number of elements in
            self._sink(1)

    def _sink(self, k):
        while (2*k <= self.n):  # can only _sink if not leaf ( 2*index at root will also be > n )
            j = 2*k  # child
            # if left child smaller than right, move j to right
            if j < self.n and self._less(self.arr, j, j+1):
                j += 1
            # don't _sink if k (current node) is larger than its two children
            if self._less(self.arr, j, k):
                break
            self._exchange(self.arr, k, j)  # otherwise _exchange
            k = j  # reset k to potentially _sink further

    def is_sorted(self):
        for i in range(1, self.n):
            if self.arr[i] < self.arr[i+1]:
                return False
        return True

    def show(self):
        print(self.arr[1:])

    @staticmethod
    def _exchange(arr, i, j):
        # alternative: t=a[i]; a[i]=a[j]; a[j]=t
        arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def _less(arr, i, j):
        return arr[i] < arr[j]

    def __len__(self):
        return self.n

    def __iter__(self):
        for i in range(1, self.n):
            yield self.arr[i]


if __name__ == '__main__':
    to_be_sorted = [8, 9, 7, 12, 23, 85, 0, -3]

    sorter = HeapSort(to_be_sorted)
    print(len(sorter))
    sorter.show()
    sorter.sort()
    print(len(sorter))
    print(f"Is Sorted: {sorter.is_sorted()}")
    sorter.show()
