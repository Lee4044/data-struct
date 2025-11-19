from src.ds import HashMap

def test_hash_map_ops():
    hm = HashMap()
    assert hm.set("a", 1) is True
    hm["b"] = 2
    assert hm.get("a") == 1
    assert hm["b"] == 2
    assert ("a", 1) in hm.items()
    assert "a" in hm.keys()
    assert hm.remove("a") is True
    assert hm.get("a") is None
    assert hm.size() == 1
    for i in range(100):
        hm.set(f"k{i}", i)
    assert hm.size() >= 50