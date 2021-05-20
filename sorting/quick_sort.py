# quicksort implementation in python (based on sedgewick and wayne, algs4 and itu.algs4 library)
import random


class QuickSort:
    """
    Implementation of Quick Sort in Ascending Order

    Analysis:
    O(n log(n)) for shuffled input 
    In-place sort (no extra memory space)
    """

    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def partition(self, lo, hi):
        """
        In-place partitioning of an array on the item v in arr[lo], such that at the end of the function
        all elements to the left of v are smaller and all elements to the right of v are greater.
        We start the search for partitioning from i+1 and j, and scan from the left end of the array until we find an entry 
        greater than (or equal) to the partioning item, and we can from the right end of the array until we find an entry less
        than (or equal to) the partioning item. The two items need to be exchanged and we continue until the two scanner indices
        cross.
        """
        i, j = lo, hi+1  # left and right pointers for scanning
        v = self.arr[lo]  # partitioning item

        while True:
            # scan from left to right and verify that elements are smaller than partioning item
            while self.arr[i+1] < v:
                i += 1
                if i == hi:
                    break
            i += 1
            # scan from right to left and verify that elements are greater than partioning item
            while v < self.arr[j-1]:
                j -= 1
                if j == lo:
                    break
            j -= 1
            # break condition of outer loop (indices cross or are equal)
            if i >= j:
                break
            # exchange elements once both inner scans find a non-match
            self.exchange(self.arr, i, j)

        # exchange partioning item into final position
        self.exchange(self.arr, lo, j)
        # return final index of partitioning item
        return j

    def sort(self):
        # random.shuffle(self.arr)
        self._sort(0, self.n-1)

    def _sort(self, lo, hi):
        # base case
        if hi <= lo:
            return
        print(f'Partioning Item: {self.arr[lo]}')
        print(self.arr)
        j = self.partition(lo, hi)
        self._sort(lo, j-1)
        self._sort(j+1, hi)

    def is_sorted(self):
        for i in range(1, self.n):
            if self.arr[i] < self.arr[i-1]:
                return False
        return True

    @staticmethod
    def _less(arr, i, j):
        return arr[i] < arr[j]

    @staticmethod
    def exchange(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def show(self):
        print(self.arr)

    def __len__(self):
        return self.n

    def __iter__(self):
        for i in range(self.n):
            yield self.arr[i]


if __name__ == '__main__':
    to_be_sorted = "E A S Y Q U E S T I O N".split()

    sorter = QuickSort(to_be_sorted)
    sorter.show()
    sorter.sort()
    print(f"Is Sorted: {sorter.is_sorted()}")
    sorter.show()
