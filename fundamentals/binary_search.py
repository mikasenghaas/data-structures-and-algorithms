# binary search implementation in python

class BinarySearch():
    """
    Binary Search implementation in Python to perform .search(item) queries in log(n) time complexity on sorted arrays
    """

    def __init__(self, arr):
        self.arr = arr

    def search(self, item):
        lo, hi = 0, len(self.arr)-1  # initialise counter low and hi
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if item < self.arr[mid]:
                hi = mid - 1
            elif item > self.arr[mid]:
                lo = mid + 1
            else:
                return mid
        return None


if __name__ == '__main__':
    find_in_here = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21]

    finder = BinarySearch(find_in_here)
    print(finder.search(8))
