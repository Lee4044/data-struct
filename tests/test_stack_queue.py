from src.ds import Stack, Queue

def test_stack_basic():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.peek() == 1
    assert s.size() == 1
    assert not s.is_empty()
    assert s.pop() == 1
    assert s.pop() is None
    assert s.is_empty()

def test_queue_basic():
    q = Queue(2)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert q.size() == 3
    assert q.dequeue() == 10
    assert q.peek() == 20
    assert q.dequeue() == 20
    assert q.dequeue() == 30
    assert q.dequeue() is None
    assert q.is_empty()