class DLNode:
    __slots__ = ("value", "prev", "next")

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push_front(self, value):
        n = DLNode(value, None, self.head)
        if self.head is not None:
            self.head.prev = n
        self.head = n
        if self.tail is None:
            self.tail = n
        self._size += 1

    def push_back(self, value):
        n = DLNode(value, self.tail, None)
        if self.tail is not None:
            self.tail.next = n
        self.tail = n
        if self.head is None:
            self.head = n
        self._size += 1

    def pop_front(self):
        if self.head is None:
            return None
        v = self.head.value
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return v

    def pop_back(self):
        if self.tail is None:
            return None
        v = self.tail.value
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
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
        curr = self.head
        while curr is not None:
            if curr.value == value:
                if curr.prev is not None:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next is not None:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev
                self._size -= 1
                return True
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
        curr = self.head
        while i < index:
            curr = curr.next
            i += 1
        n = DLNode(value, curr.prev, curr)
        if curr.prev is not None:
            curr.prev.next = n
        curr.prev = n
        self._size += 1
        return True

    def reverse(self):
        curr = self.head
        self.head, self.tail = self.tail, self.head
        while curr is not None:
            curr.prev, curr.next = curr.next, curr.prev
            curr = curr.prev

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

    def to_list_reverse(self):
        out = []
        curr = self.tail
        while curr is not None:
            out.append(curr.value)
            curr = curr.prev
        return out