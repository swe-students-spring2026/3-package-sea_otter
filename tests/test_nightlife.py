from pathlib import Path
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pynyc import find_nightlife_activity, list_nightlife_places


def test_list_nightlife_places_returns_real_dancing_options():
    places = list_nightlife_places("dancing")

    assert len(places) >= 4
    assert any(place["name"] == "House of Yes" for place in places)
    assert all(place["website"].startswith("http") for place in places)


def test_find_nightlife_activity_supports_aliases(monkeypatch):
    monkeypatch.setattr( 
        "pynyc.pynyc.random.choice",
        lambda places: places[0],
    )

    choice = find_nightlife_activity("karaoke")

    assert choice == {
        "vibe": "singing",
        "activity_type": "karaoke",
        "name": "Planet Rose",
        "website": "https://www.planetrosenyc.com/",
    }


def test_invalid_vibe_raises_clear_error():
    with pytest.raises(ValueError, match="Unsupported vibe"):
        find_nightlife_activity("quiet reading")
