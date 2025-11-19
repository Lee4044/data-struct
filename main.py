from src.ds import Stack, Queue, SinglyLinkedList, BinarySearchTree, HashMap

s = Stack()
s.push(1)
s.push(2)
print(s.pop())
print(s.peek())
print(s.size())

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())
print(q.peek())
print(q.size())

ll = SinglyLinkedList()
ll.push_back(3)
ll.push_front(2)
ll.push_back(4)
print(ll.to_list())
ll.remove(3)
print(ll.to_list())
ll.reverse()
print(ll.to_list())

bst = BinarySearchTree()
for v in [5, 2, 8, 1, 3, 7, 9]:
    bst.insert(v)
print(bst.inorder())
print(bst.contains(3))
bst.delete(5)
print(bst.inorder())
print(bst.height())

hm = HashMap()
hm.set("a", 1)
hm["b"] = 2
print(hm.get("a"))
print(hm["b"])
print(hm.items())
del hm["a"]
print(hm.keys())