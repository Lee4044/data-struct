from src.ds import SinglyLinkedList, DoublyLinkedList

def test_singly_linked_list():
    ll = SinglyLinkedList()
    ll.push_back(1)
    ll.push_front(0)
    ll.push_back(2)
    assert ll.to_list() == [0, 1, 2]
    assert ll.find(1) == 1
    assert ll.remove(1) is True
    assert ll.to_list() == [0, 2]
    ll.reverse()
    assert ll.to_list() == [2, 0]
    assert ll.size() == 2

def test_doubly_linked_list():
    dl = DoublyLinkedList()
    dl.push_front(1)
    dl.push_back(2)
    dl.insert_at(1, 3)
    assert dl.to_list() == [1, 3, 2]
    assert dl.find(3) == 1
    assert dl.remove(3) is True
    assert dl.to_list() == [1, 2]
    assert dl.pop_front() == 1
    assert dl.pop_back() == 2
    assert dl.pop_back() is None
    dl.push_back(4)
    dl.push_back(5)
    dl.reverse()
    assert dl.to_list() == [5, 4]
    assert dl.to_list_reverse() == [4, 5]