# shell sort api in python (based on sedgewick and wayne, algs4 and itu.algs4 library)

class ShellSort():
    """
    Implementation of Shell Sort in Ascending Order
    """

    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.sort()

    @staticmethod
    def exchange(arr, i, j):
        # alternative: t=a[i]; a[i]=a[j]; a[j]=t
        arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def less(arr, i, j):
        return arr[i] < arr[j]

    def sort(self):
        h = 1
        while h < self.n/3:
            h = 3*h + 1
        while h >= 1:
            print(h)
            for i in range(h, self.n):
                print(i)
                print(self.arr)
                for j in range(i, h-1, -h):
                    if self.less(self.arr, j, j-h):
                        print(f'Exchanged: {self.arr[j]} and {self.arr[j-h]}')
                        self.exchange(self.arr, j, j-h)
            h = h//3

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
    to_be_sorted = list(reversed(list(range(20))))
    sorter = ShellSort(to_be_sorted)
    sorter.show()
    print(f"Is Sorted: {sorter.is_sorted()}")
