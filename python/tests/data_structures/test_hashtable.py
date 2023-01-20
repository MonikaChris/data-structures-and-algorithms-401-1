import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


#@pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item)

    expected = [["listen", "to me"], ["ahmad", 30], ["silent", True]]

    assert actual == expected

#@pytest.mark.skip("TODO")
def test_has_true():
    hashtable = Hashtable()
    hashtable.set("apple", 'red')
    hashtable.set("banana", 'yellow')

    assert hashtable.has("apple") == True

#@pytest.mark.skip("TODO")
def test_has_false():
    hashtable = Hashtable()
    hashtable.set("apple", 'red')
    hashtable.set("banana", 'yellow')

    assert hashtable.has("pear") == False

#@pytest.mark.skip("TODO")
def test_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "red")
    hashtable.set("banana", "yellow")
    hashtable.set("orange", "orange")

    actual = hashtable.keys()
    expected = ["banana", "apple", "orange"]

    assert actual == expected

@pytest.mark.skip("TODO")
def test_get_value_not_found():
    hashtable = Hashtable()
    hashtable.set("apple", "red")
    hashtable.set("banana", "yellow")
    hashtable.set("orange", "orange")

    assert hashtable.get("pear") == None
