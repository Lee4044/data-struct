class Queue:
    def __init__(self, capacity=16):
        self._capacity = max(2, int(capacity))
        self._data = [None] * self._capacity
        self._head = 0
        self._tail = 0
        self._size = 0

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[(self._head + i) % self._capacity]
        self._data = new_data
        self._capacity = new_capacity
        self._head = 0
        self._tail = self._size

    def enqueue(self, value):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._tail] = value
        self._tail = (self._tail + 1) % self._capacity
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            return None
        value = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return value

    def peek(self):
        if self._size == 0:
            return None
        return self._data[self._head]

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size