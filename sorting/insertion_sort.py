# insertion sort api in python (based on sedgewick and wayne, algs4 and itu.algs4 library)

class InsertionSort():
    """
    Implementation of Insertion Sort in Ascending Order

    Analysis:
    Worst/Average Case: O(n^2)
    Best-Case: O(n)
    Stable Sorting (duplicates are kept in original order)
    Well-Performing on partially sorted input (only makes n compares to check if sorted)
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
        for i in range(1, self.n):
            for j in range(i, 0, -1):
                if self.arr[j] > self.arr[j-1]:  # element in correct position
                    break
                self.exchange(self.arr, j, j-1)

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

    sorter = InsertionSort(to_be_sorted)
    sorter.show()
    print(f"Is Sorted: {sorter.is_sorted()}")
    sorter.show()
