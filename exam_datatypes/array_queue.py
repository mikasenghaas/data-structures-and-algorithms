class Y:
    def __init__(self):
        self.lo = self.hi = self.N = 0
        self.A = [None]*1

    def insert(self, element):
        self.A[self.hi] = element
        self.hi += 1
        if self.hi == len(self.A):
            self.hi = 0
        self.N += 1
        if self.N == len(self.A):
            self.rebuild()

    def remove(self):
        out = self.A[self.lo]
        self.A[self.lo] = None
        self.lo += 1
        if self.lo == len(self.A):
            self.lo = 0
        self.N -= 1
        return out

    def rebuild(self):
        temp = [None] * 2*len(self.A)
        for i in range(self.N):
            temp[i] = self.A[(i + self.lo) % len(self.A)]
        self.A = temp
        self.lo = 0
        self.hi = self.N

    def __str__(self):
        string = '[ '
        for i in range(len(self.A)):
            string += f'{self.A[i]} '
        return string + ']'


if __name__ == '__main__':
    y = Y()
    z = Y()
    w = z
    # w.insert(3)
    z.insert(1)
    y.insert(2)
    a = z.remove()
    b = y.remove()
    print(a, b)
