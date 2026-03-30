import pytest

from pynyc import find_restaurant as fr
from pynyc.pynyc import restaurant_list, michelin_restaurants_list

INVALID_MSG = "Google and ask it to generate one restaurant for this cuisine, we don't have a great choice of this yet oops."


# valid cuisine, no michelin
def test_find_restaurant_valid_cuisine():
    # asking for italian food should return a real restaurant name
    result = fr("italian")
    assert result is not None
    assert isinstance(result, str)
    assert result in restaurant_list["italian"].values()


# valid cuisine, michelin=True
def test_find_restaurant_michelin_valid_cuisine():
    # asking for japanese michelin food should return a real michelin restaurant
    result = fr("japanese", michelin=True)
    assert result is not None
    assert isinstance(result, str)
    assert result in michelin_restaurants_list["japanese"].values()


# input is case-insensitive (uppercase should still work)
def test_find_restaurant_case_insensitive():
    # typing in all caps should still work the same as lowercase
    result = fr("ITALIAN")
    assert result is not None
    assert isinstance(result, str)
    assert result in restaurant_list["italian"].values()


# invalid cuisine, no michelin
def test_find_restaurant_invalid_cuisine():
    # a made-up cuisine should return the fallback message, not crash
    result = fr("klingon")
    assert result is not None
    assert isinstance(result, str)
    assert result == INVALID_MSG


# invalid cuisine, michelin=True
def test_find_restaurant_michelin_invalid_cuisine():
    # a made-up cuisine with michelin=True should also return the fallback message
    result = fr("klingon", michelin=True)
    assert result is not None
    assert isinstance(result, str)
    assert result == INVALID_MSG

