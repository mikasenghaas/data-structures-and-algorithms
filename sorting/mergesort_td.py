# top-down mergesort api in python (based on sedgewick and wayne, algs4 and itu.algs4 library)

class MergeSortTD():
    """
    Implementation of Mege Sort in Ascending Order

    Analysis:
    """

    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    @staticmethod
    def merge(arr, aux, lo, mid, hi):
        i, j = lo, mid+1  # pointers to start of left and right half

        # copy contents into auxiliary array
        for k in range(lo, hi+1):
            aux[k] = arr[k]

        # merge back to original arr
        for k in range(lo, hi+1):
            # left half exhausted, take from left
            if i > mid:
                arr[k] = aux[j]
                j += 1
            # right half exhausted, take from left
            elif j > hi:
                arr[k] = aux[i]
                i += 1
            # key on right half is smaller than left (take from right)
            elif aux[j] < aux[i]:
                arr[k] = aux[j]
                j += 1
            # key on left half is smaller than right (take from left)
            else:
                arr[k] = aux[i]
                i += 1
        return arr

    def sort(self):
        aux = [None] * self.n
        self._sort(self.arr, aux, 0, self.n - 1)

    # @staticmethod
    def _sort(self, arr, aux,  lo, hi):
        if hi <= lo:
            return
        mid = lo + (hi - lo) // 2

        # sort left half recursively self._sort(arr, aux, mid+1, hi)  # sort right half recursively
        self._sort(arr, aux, lo, mid)
        self._sort(arr, aux, mid+1, hi)
        print(f'merge: {lo}, {mid}, {hi}')
        MergeSortTD.merge(arr, aux, lo, mid, hi)
        print(self.arr)

    def is_sorted(self):
        for i in range(1, self.n):
            if self.arr[i] < self.arr[i-1]:
                return False
        return True

    def show(self):
        print(self.arr)

    def __len__(self):
        return self.n

    def __iter__(self):
        for i in range(self.n):
            yield self.arr[i]


# test client
if __name__ == '__main__':
    to_be_sorted = "E A S Y Q U E S T I O N".split()

    sorter = MergeSortTD(to_be_sorted)
    sorter.show()
    sorter.sort()
    print(f"Is Sorted: {sorter.is_sorted()}")
    sorter.show()
