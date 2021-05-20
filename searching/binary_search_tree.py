# binary search tree (bst) python implementation

class BSTNode:
    def __init__(self, key=None, val=None, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.size = 1

    def __str__(self):
        return f'{self.key}, {self.val}'


class BinarySearchTreeDict:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.size() == 0

    def size(self):
        if self.root != None:
            return self.root.size
        return 0

    def _size(self, node):
        if node == None:
            return 0
        return node.size

    def get(self, key):
        if key == None:
            raise ValueError
        return self._get(self.root, key)

    def _get(self, curr, key):
        # base case
        if curr == None:
            return
        # recursive search further
        if key < curr.key:
            # to left if curr is smaller than key
            return self._get(curr.left, key)
        elif key > curr.key:
            # to right if curr is greater than key
            return self._get(curr.right, key)
        else:  # search hit
            return curr.val

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, curr, key, val):
        if curr == None:
            return BSTNode(key, val)
        else:
            if key < curr.key:
                curr.left = self._put(curr.left, key, val)
            elif key > curr.key:
                curr.right = self._put(curr.right, key, val)
            else:
                curr.val = val
            curr.size = self._size(curr.left) + self._size(curr.right) + 1
            return curr

    def min(self):
        if self.size() == 0:
            raise ValueError
        return self._min(self.root).key

    @staticmethod
    def _min(node):
        if node.left == None:
            return node
        return BinarySearchTreeDict._min(node.left)

    def max(self):
        if self.size() == 0:
            raise ValueError
        return self._max(self.root).key

    @staticmethod
    def _max(node):
        if node.right == None:
            return node
        return BinarySearchTreeDict._max(node.right)

    def __str__(self):
        pass


if __name__ == '__main__':
    dictionary = BinarySearchTreeDict()
    dictionary.put('name', 'mika')
    dictionary.put('age', 19)
    print(dictionary.get('name'))
    print(dictionary.size())
    print(dictionary.min())
