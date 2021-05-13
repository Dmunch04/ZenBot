from zenbot.utils import Cache


def test_cache():
    cache = Cache(int)
    cache.put("a", 5)
    cache.put("b", 10)
    cache.put("c", 15)

    assert cache.get("a") == 5
    assert cache.get("b") == 10
    assert cache.get("c") == 15
    assert len(cache) == 3

    cache.remove("c")

    assert not cache.has("c")
    assert len(cache) == 2
    assert cache.get("d", default=20) == 20
