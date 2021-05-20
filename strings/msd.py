# python implementation of msd (most significant digit string sorting)

class MSD:
    def __init__(self, arr, w):
        self.R = 256  # alphabet
        self.cutoff = 0  # cutoff for small subarrays
        self.arr = arr  # to be sorted strings
        self.n = len(arr)  # number of strings to sort
        self.w = w  # word length

    def sort(self):
        aux = [None] * self.n
        self._sort(0, self.n - 1, 0, aux, self.R)

    def _sort(self, lo, hi, d, aux, radix):
        # if cutoff is reached (subarray to sort is smaller than cutoff), sort using insertion sort and return from recursive call
        if hi <= lo + self.cutoff:
            #self._insertion(lo, hi, d)
            return

        # compute frequency counts
        count = [0] * (radix + 2)
        for i in range(lo, hi + 1):
            # get number representation of character
            ch = self.char_at(self.arr[i], d)
            count[ch + 2] += 1

        # compute cumulates
        for r in range(radix + 1):
            count[r + 1] += count[r]

        # move data
        for i in range(lo, hi + 1):
            ch = self.char_at(self.arr[i], d)
            aux[count[ch + 1]] = self.arr[i]
            count[ch + 1] += 1

        # copy back
        for i in range(lo, hi + 1):
            self.arr[i] = aux[i - lo]

        #print(d, self.arr)

        # recursively sort for each character (excludes sentinel -1)
        for r in range(radix):
            # if count[r] < count[r+1]-1:
            #    print(chr(r))
            self._sort(lo + count[r], lo +
                       count[r + 1] - 1, d + 1, aux, radix)

    @staticmethod
    def char_at(s, d):
        if d >= len(s):
            return -1
        return ord(s[d])

    def _less(self, a, b, d):
        return a[d] < b[d]

    def _insertion(self, lo, hi, d):
        for i in range(lo, hi + 1):
            j = i
            while j > lo and self._less(self.arr[j], self.arr[j - 1], d):
                # exchange if left smaller than right
                self.arr[j], self.arr[j - 1] = self.arr[j - 1], self.arr[j]
                j -= 1

    def show(self):
        print(self.arr)


if __name__ == '__main__':
    to_be_sorted = ['she',
                    'shells',
                    'seashells',
                    'by',
                    'the',
                    'sea',
                    'shore',
                    'the',
                    'she',
                    'shore',
                    'are',
                    'surely',
                    'seashells',
                    'sells',
                    'sells']

    sorter = MSD(to_be_sorted, len(to_be_sorted[0]))

    sorter.show()
    sorter.sort()
    sorter.show()
