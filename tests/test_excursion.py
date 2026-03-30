import pytest
import pynyc
from pynyc.pynyc import EXCURSION_OPTIONS

def test_list_excursions_returns_expected_keys():
    for category in ("nature", "historic", "coastal"):
        rows = pynyc.list_excursions(category)
        assert len(rows) >= 2
        for row in rows:
            assert set(row.keys()) == {"name", "location", "website"}
            assert row["website"].startswith("http")
            assert len(row["location"]) > 5

def test_find_excursion_alias_outdoors_matches_nature():
    assert pynyc.list_excursions("outdoors") == pynyc.list_excursions("nature")

def test_find_excursion_invalid_category():
    with pytest.raises(ValueError, match="Unknown category"):
        pynyc.find_excursion("volcano")

def test_find_excursion_is_subset_of_list(monkeypatch):
    monkeypatch.setattr(
        "pynyc.pynyc.random.choice",
        lambda xs: xs[0],
    )
    picked = pynyc.find_excursion("coastal")
    listed = pynyc.list_excursions("coastal")
    assert picked in listed

def test_excursion_urls_are_unique_per_category():
    for category, bundle in EXCURSION_OPTIONS.items():
        urls = [x["website"] for x in bundle["places"]]
        assert len(urls) == len(set(urls)), f"duplicate URL in {category}"