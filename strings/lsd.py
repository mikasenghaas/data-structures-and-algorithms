# python implementation of lsd (least significant digit string sorting)

class LSD:
    def __init__(self, arr):
        self.R = 256  # alphabet
        self.arr = arr  # to be sorted strings
        self.n = len(arr)  # number of strings to sort
        self.w = len(arr[0])  # word length

    def sort(self):
        aux = [''] * self.n

        for d in range(self.w-1, -1, -1):
            count = [0] * (self.R + 1)

            # compute frequency
            for i in range(self.n):
                ch = ord(self.arr[i][d])
                count[ch + 1] += 1

            # convert to indices
            for r in range(self.R):
                count[r+1] += count[r]

            # distribute
            for i in range(self.n):
                ch = ord(self.arr[i][d])
                aux[count[ch]] = self.arr[i]
                count[ch] += 1

            # back copy
            for i in range(self.n):
                self.arr[i] = aux[i]
            #print(d, self.arr)

    def show(self):
        print(self.arr)


class ExtendedLSD:
    def __init__(self, arr):
        self.R = 256  # alphabet
        self.arr = arr  # to be sorted strings
        self.n = len(arr)  # number of strings to sort
        self.w = self.find_max_w()  # word length

    def sort(self):
        aux = [''] * self.n

        for d in range(self.w-1, -1, -1):
            count = [0] * (self.R + 1)

            # compute frequency
            for i in range(self.n):
                ch = ord(self.char_at(self.arr[i], d))
                count[ch + 1] += 1

            # convert to indices
            for r in range(self.R):
                count[r+1] += count[r]

            # distribute
            for i in range(self.n):
                ch = ord(self.char_at(self.arr[i], d))
                aux[count[ch]] = self.arr[i]
                count[ch] += 1

            # back copy
            for i in range(self.n):
                self.arr[i] = aux[i]
            #print(d, self.arr)

    def find_max_w(self):
        # find maximum length string
        max_length = len(self.arr[0])
        for i in range(1, self.n):
            if len(self.arr[i]) > max_length:
                max_length = len(self.arr[i])
        return max_length

    @staticmethod
    def char_at(s, d):
        if d >= len(s):
            return '0'
        return s[d]

    def show(self):
        print(self.arr)


if __name__ == '__main__':
    to_be_sorted = ['aa',
                    'a',
                    'AAA',
                    'A',
                    'av']

    sorter = ExtendedLSD(to_be_sorted)

    sorter.show()
    sorter.sort()
    sorter.show()
