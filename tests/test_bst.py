from src.ds import BinarySearchTree

def test_bst_ops():
    bst = BinarySearchTree()
    for v in [5, 2, 8, 1, 3, 7, 9]:
        assert bst.insert(v) is True
    assert bst.contains(3) is True
    assert bst.contains(4) is False
    assert bst.min() == 1
    assert bst.max() == 9
    assert bst.inorder() == [1, 2, 3, 5, 7, 8, 9]
    assert bst.delete(5) is True
    assert bst.inorder() == [1, 2, 3, 7, 8, 9]
    assert bst.height() >= 2
    assert bst.size() == 6