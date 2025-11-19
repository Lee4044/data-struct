from src.ds import MinHeap, MaxHeap, Graph

def test_min_heap():
    h = MinHeap()
    for v in [5, 1, 3, 2, 4]:
        h.push(v)
    assert h.peek() == 1
    assert [h.pop(), h.pop(), h.pop(), h.pop(), h.pop()] == [1, 2, 3, 4, 5]
    assert h.pop() is None

def test_max_heap():
    h = MaxHeap()
    for v in [5, 1, 3, 2, 4]:
        h.push(v)
    assert h.peek() == 5
    assert [h.pop(), h.pop(), h.pop(), h.pop(), h.pop()] == [5, 4, 3, 2, 1]
    assert h.pop() is None

def test_graph_bfs_dfs():
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    bfs = g.bfs("A")
    dfs = g.dfs("A")
    assert "A" in bfs and "B" in bfs and "C" in bfs and "D" in bfs
    assert "A" in dfs and "B" in dfs and "C" in dfs and "D" in dfs