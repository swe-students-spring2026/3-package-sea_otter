from pynyc import pynyc
from pynyc.pynyc import ACTIVITIES

def test_activity_rainy():
    result = pynyc.find_activity("rainy")
    assert result is not None
    assert result in ACTIVITIES["rainy"]

def test_activity_sunny():
    result = pynyc.find_activity("sunny")
    assert result is not None
    assert result in ACTIVITIES["sunny"]

def test_activity_freezing():
    result = pynyc.find_activity("freezing")
    assert result is not None
    assert result in ACTIVITIES["freezing"]

def test_activity_hot():
    result = pynyc.find_activity("hot")
    assert result is not None
    assert result in ACTIVITIES["hot"]

def test_activity_perfect():
    result = pynyc.find_activity("perfect")
    assert result is not None
    assert result in ACTIVITIES["perfect"]

def test_activity_cold():
    result = pynyc.find_activity("cold")
    assert result is not None
    assert result in ACTIVITIES["freezing"]

def test_activity_case_insensitive():
    result = pynyc.find_activity("RAINY")
    assert result is not None
    assert "not valid" not in result
    assert result in ACTIVITIES["rainy"]  

def test_activity_invalid():
    result = pynyc.find_activity("tornado")
    assert result is not None
    assert isinstance(result, str)
    assert "not valid" in result