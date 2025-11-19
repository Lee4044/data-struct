class BSTNode:
    __slots__ = ("key", "left", "right")

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self._size = 0

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
            self._size += 1
            return True
        curr = self.root
        while True:
            if key == curr.key:
                return False
            if key < curr.key:
                if curr.left is None:
                    curr.left = BSTNode(key)
                    self._size += 1
                    return True
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BSTNode(key)
                    self._size += 1
                    return True
                curr = curr.right

    def contains(self, key):
        curr = self.root
        while curr is not None:
            if key == curr.key:
                return True
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def min(self):
        if self.root is None:
            return None
        curr = self.root
        while curr.left is not None:
            curr = curr.left
        return curr.key

    def max(self):
        if self.root is None:
            return None
        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.key

    def _delete_recursive(self, node, key):
        if node is None:
            return None, False
        if key < node.key:
            node.left, deleted = self._delete_recursive(node.left, key)
            return node, deleted
        if key > node.key:
            node.right, deleted = self._delete_recursive(node.right, key)
            return node, deleted
        if node.left is None and node.right is None:
            return None, True
        if node.left is None:
            return node.right, True
        if node.right is None:
            return node.left, True
        succ_parent = node
        succ = node.right
        while succ.left is not None:
            succ_parent = succ
            succ = succ.left
        node.key = succ.key
        if succ_parent.left is succ:
            succ_parent.left, _ = self._delete_recursive(succ_parent.left, succ.key)
        else:
            succ_parent.right, _ = self._delete_recursive(succ_parent.right, succ.key)
        return node, True

    def delete(self, key):
        self.root, deleted = self._delete_recursive(self.root, key)
        if deleted:
            self._size -= 1
        return deleted

    def inorder(self):
        out = []
        stack = []
        curr = self.root
        while curr is not None or stack:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            out.append(curr.key)
            curr = curr.right
        return out

    def preorder(self):
        out = []
        if self.root is None:
            return out
        stack = [self.root]
        while stack:
            node = stack.pop()
            out.append(node.key)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return out

    def postorder(self):
        out = []
        stack = []
        last = None
        curr = self.root
        while curr is not None or stack:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                peek = stack[-1]
                if peek.right is not None and last is not peek.right:
                    curr = peek.right
                else:
                    out.append(peek.key)
                    last = stack.pop()
        return out

    def height(self):
        def h(n):
            if n is None:
                return -1
            a = h(n.left)
            b = h(n.right)
            return 1 + (a if a > b else b)
        return h(self.root)

    def size(self):
        return self._size