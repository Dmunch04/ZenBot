from zenbot.models import DBTestObject, OtherDBTestObject, ImprovedDBObject


def test_test_object_new():
    db = {"id2": {"a": 7, "b": 10, "c": 11}}

    if "id" in db:
        obj = DBTestObject.from_dict(db["id"])
    else:
        obj = DBTestObject.new()

    assert obj is not None
    assert obj.a == 0
    assert obj.b == 1
    assert obj.c == 2


def test_test_object_exists():
    db = {"id": {"a": 7, "b": 10, "c": 11}}

    if "id" in db:
        obj = DBTestObject.from_dict(db["id"])
    else:
        obj = DBTestObject.new()

    assert obj is not None
    assert obj.a == 7
    assert obj.b == 10
    assert obj.c == 11


def test_other_test_object_new():
    db = {"id2": {"a": 7, "b": 10, "c": 11}}

    if "id" in db:
        obj = OtherDBTestObject.from_dict(db["id"])
    else:
        obj = OtherDBTestObject.new(DBTestObject.new())

    assert obj is not None
    assert obj.a == 0
    assert obj.b == 1
    assert obj.c == "2"


def test_other_test_object_exists():
    db = {"id": {"a": 7, "b": 10, "c": 11}}

    if "id" in db:
        obj = OtherDBTestObject.from_dict(db["id"])
    else:
        obj = OtherDBTestObject.new(DBTestObject.new())

    assert obj is not None
    assert obj.a == 7
    assert obj.b == 10
    assert obj.c == "11"


def test_improved_test_object_new():
    db = {"id2": {"a": 7, "b": 10, "c": 11}}

    if "id" in db:
        obj = ImprovedDBObject.from_dict(db["id"])
    else:
        obj = ImprovedDBObject.new(DBTestObject.new())

    assert obj is not None
    assert obj.a == 0
    assert obj.b == 1
    assert obj.c == 2


def test_improved_test_object_exists():
    db = {"id": {"a": 7, "b": 10, "c": 11}}

    if "id" in db:
        obj = ImprovedDBObject.from_dict(db["id"])
    else:
        obj = ImprovedDBObject.new(DBTestObject.new())

    assert obj is not None
    assert obj.a == 7
    assert obj.b == 10
    assert obj.c == 11
