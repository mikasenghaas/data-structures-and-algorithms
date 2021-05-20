# key-indexed counting for sorting strings of length 1

class KeyIndexedCounting:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.R = 256

    def sort(self):
        # count frequency
        count = [0] * (self.R + 1)  # len 6 (last index 5)
        aux = [None] * self.n

        # compute frequency count
        for i in range(self.n):
            ch = ord(str(self.arr[i]))
            count[ch + 1] += 1

        # convert frequency to indices
        for r in range(len(count)-1):
            count[r+1] += count[r]

        # distribute data
        for i in range(self.n):
            ch = ord(str(self.arr[i]))
            aux[count[ch]] = self.arr[i]
            count[ch] += 1

        # copy back
        self.arr = aux

    def is_sorted(self):
        for i in range(1, self.n):
            if ord(str(self.arr[i-1])) > ord(str(self.arr[i])):
                return False
        return True

    def show(self):
        print(self.arr)

    def __len__(self):
        return self.n

    def __iter__(self):
        for i in range(self.n):
            yield self.arr[i]


if __name__ == '__main__':
    to_be_sorted = [1, 2, 3, 4, 5, 2, 2, 4, 3, 1, 4, 5, 'a', 'b', 'A']

    sorter = KeyIndexedCounting(to_be_sorted)

    print(sorter.is_sorted())
    sorter.sort()
    sorter.show()
    print(sorter.is_sorted())
