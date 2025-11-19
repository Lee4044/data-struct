class Node:
    __slots__ = ("value", "next")

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push_front(self, value):
        n = Node(value, self.head)
        self.head = n
        if self.tail is None:
            self.tail = n
        self._size += 1

    def push_back(self, value):
        n = Node(value, None)
        if self.tail is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self._size += 1

    def pop_front(self):
        if self.head is None:
            return None
        v = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return v

    def pop_back(self):
        if self.head is None:
            return None
        if self.head.next is None:
            v = self.head.value
            self.head = None
            self.tail = None
            self._size -= 1
            return v
        prev = None
        curr = self.head
        while curr.next is not None:
            prev = curr
            curr = curr.next
        v = curr.value
        prev.next = None
        self.tail = prev
        self._size -= 1
        return v

    def find(self, value):
        idx = 0
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return idx
            curr = curr.next
            idx += 1
        return -1

    def remove(self, value):
        prev = None
        curr = self.head
        while curr is not None:
            if curr.value == value:
                if prev is None:
                    self.head = curr.next
                    if self.head is None:
                        self.tail = None
                else:
                    prev.next = curr.next
                    if prev.next is None:
                        self.tail = prev
                self._size -= 1
                return True
            prev = curr
            curr = curr.next
        return False

    def insert_at(self, index, value):
        if index < 0 or index > self._size:
            return False
        if index == 0:
            self.push_front(value)
            return True
        if index == self._size:
            self.push_back(value)
            return True
        i = 0
        prev = None
        curr = self.head
        while i < index:
            prev = curr
            curr = curr.next
            i += 1
        n = Node(value, curr)
        prev.next = n
        self._size += 1
        return True

    def reverse(self):
        prev = None
        curr = self.head
        self.tail = self.head
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def to_list(self):
        out = []
        curr = self.head
        while curr is not None:
            out.append(curr.value)
            curr = curr.next
        return out