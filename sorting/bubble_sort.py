# bubble sort api in python (based on sedgewick and wayne, algs4 and itu.algs4 library)

class BubbleSort():
    """
    Implementation of Bubble Sort in Ascending Order

    Analysis:
    Worst/Average Case: O(n^2)
    Best-Case: O(n)
    Solely used for educational purposes
    """

    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.sort()

    @staticmethod
    def exchange(arr, i, j):
        # alternative: t=a[i]; a[i]=a[j]; a[j]=t
        arr[i], arr[j] = arr[j], arr[i]

    def sort(self):
        for n in range(self.n-1, 0, -1):
            for i in range(n):
                if self.arr[i] > self.arr[i+1]:
                    self.exchange(self.arr, i, i+1)

    def is_sorted(self):
        for i in range(self.n-1):
            if self.arr[i] > self.arr[i+1]:
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
    to_be_sorted = [8, 9, 7, 12, 23, 85, 0, -3]

    sorter = BubbleSort(to_be_sorted)
    sorter.show()
    print(f"Is Sorted: {sorter.is_sorted()}")
