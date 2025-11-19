class MinHeap:
    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)
        i = len(self._data) - 1
        while i > 0:
            p = (i - 1) // 2
            if self._data[i] < self._data[p]:
                self._data[i], self._data[p] = self._data[p], self._data[i]
                i = p
            else:
                break

    def pop(self):
        n = len(self._data)
        if n == 0:
            return None
        root = self._data[0]
        last = self._data.pop()
        if n > 1:
            self._data[0] = last
            i = 0
            while True:
                l = 2 * i + 1
                r = 2 * i + 2
                smallest = i
                if l < len(self._data) and self._data[l] < self._data[smallest]:
                    smallest = l
                if r < len(self._data) and self._data[r] < self._data[smallest]:
                    smallest = r
                if smallest == i:
                    break
                self._data[i], self._data[smallest] = self._data[smallest], self._data[i]
                i = smallest
        return root

    def peek(self):
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)


class MaxHeap:
    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)
        i = len(self._data) - 1
        while i > 0:
            p = (i - 1) // 2
            if self._data[i] > self._data[p]:
                self._data[i], self._data[p] = self._data[p], self._data[i]
                i = p
            else:
                break

    def pop(self):
        n = len(self._data)
        if n == 0:
            return None
        root = self._data[0]
        last = self._data.pop()
        if n > 1:
            self._data[0] = last
            i = 0
            while True:
                l = 2 * i + 1
                r = 2 * i + 2
                largest = i
                if l < len(self._data) and self._data[l] > self._data[largest]:
                    largest = l
                if r < len(self._data) and self._data[r] > self._data[largest]:
                    largest = r
                if largest == i:
                    break
                self._data[i], self._data[largest] = self._data[largest], self._data[i]
                i = largest
        return root

    def peek(self):
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)