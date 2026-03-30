from pynyc import get_cafe

def test_get_cafe_morning():
    result = get_cafe("morning")
    assert result is not None

def test_get_cafe_afternoon():
    result = get_cafe("afternoon")
    assert result is not None

def test_get_cafe_evening():
    result = get_cafe("evening")
    assert result is not None

def test_get_cafe_case_insensitive():
    result = get_cafe("MORNING")
    assert result is not None

def test_get_cafe_invalid():
    result = get_cafe("midnight")
    assert isinstance(result, str)
    assert "not valid" in result
    