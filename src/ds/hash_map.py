class HashMap:
    def __init__(self, initial_capacity=8):
        c = 1
        while c < initial_capacity:
            c <<= 1
        self._capacity = max(8, c)
        self._size = 0
        self._buckets = [[] for _ in range(self._capacity)]
        self._load_factor = 0.75

    def _index(self, key):
        return hash(key) & (self._capacity - 1)

    def _resize(self, new_capacity):
        old_items = self.items()
        c = 1
        while c < new_capacity:
            c <<= 1
        self._capacity = max(8, c)
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        for k, v in old_items:
            self.set(k, v)

    def set(self, key, value):
        idx = self._index(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return True
        bucket.append((key, value))
        self._size += 1
        if self._size > int(self._capacity * self._load_factor):
            self._resize(self._capacity * 2)
        return True

    def get(self, key, default=None):
        idx = self._index(key)
        bucket = self._buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        return default

    def remove(self, key):
        idx = self._index(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return True
        return False

    def keys(self):
        out = []
        for b in self._buckets:
            for k, _ in b:
                out.append(k)
        return out

    def values(self):
        out = []
        for b in self._buckets:
            for _, v in b:
                out.append(v)
        return out

    def items(self):
        out = []
        for b in self._buckets:
            for k, v in b:
                out.append((k, v))
        return out

    def size(self):
        return self._size

    def __len__(self):
        return self._size

    def __contains__(self, key):
        return self.get(key, None) is not None

    def __getitem__(self, key):
        v = self.get(key, None)
        if v is None:
            raise KeyError(key)
        return v

    def __setitem__(self, key, value):
        self.set(key, value)

    def __delitem__(self, key):
        if not self.remove(key):
            raise KeyError(key)