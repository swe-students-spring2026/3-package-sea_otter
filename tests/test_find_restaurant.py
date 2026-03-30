import pytest

from pynyc import find_restaurant as fr
from pynyc.pynyc import restaurant_list


@pytest.mark.parametrize("cuisine", list(restaurant_list.keys()))
def test_find_restaurant_returns_entry_from_cuisine(cuisine):
    result = fr(cuisine)
    assert result is not None
    assert result in restaurant_list[cuisine].values()


@pytest.mark.parametrize("cuisine", list(restaurant_list.keys()))
def test_find_restaurant_lowercase_cuisine_fails(cuisine):
    with pytest.raises(KeyError):
        fr(cuisine.lower())

