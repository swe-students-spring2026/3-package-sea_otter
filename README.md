# Python Package Exercise

[![workflow_run](https://github.com/swe-students-spring2026/3-package-sea_otter/actions/workflows/event-logger.yml/badge.svg)](https://github.com/swe-students-spring2026/3-package-sea_otter/actions/workflows/event-logger.yml)

## Description
A python package that returns fun NYC plans and recommendations! 

## Github

[Github Link](https://github.com/swe-students-spring2026/3-package-sea_otter)

## Developers

[Albert Chen](https://github.com/azc9673)
[Blake Chang](https://github.com/louisvcarpet)
[Valeria Chang](https://github.com/ValeriaChang)
[Vincent Campanaro](https://github.com/vincentcamp)
[Sasha Cartagena](https://github.com/sashacartagena)

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

---

## Installing the Package

Install `pynyc` directly from PyPI:

```bash
pip install pynyc
```

---

## `find_restaurant(cuisine, michelin=False)`

Returns a restaurant name in New York City for a given cuisine type.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `cuisine` | `str` | Yes | The type of food you want (e.g. `"italian"`, `"japanese"`) |
| `michelin` | `bool` | No | Set to `True` to get a Michelin-listed restaurant. Default is `False` |

### Example usage

```python
import pynyc

# Generate any Italian restaurant
restaurant = pynyc.find_restaurant("italian")
print(f"Go to {restaurant}")

# Help you to pick a Michelin-listed Japanese restaurant
restaurant = pynyc.find_restaurant("japanese", michelin=True)
print(f"Go to {restaurant}")

```

Input is **case-insensitive** for better efficiency— `"ITALIAN"`, `"Italian"`, and `"italian"` all work the same.

## `find_activity(weather)`

Returns an activity recommendation in NYC based on the weather.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `weather` | `str` | Yes | The weather outside (e.g. `"hot"`, `"freezing"`, `"perfect"`, `"rainy"`) |

Input is **case-insensitive** - `"sunny"`, `"Sunny"`, and `"SUNNY"` all work the same.

See the full working example in [example.py](./example.py).

### Example usage

```python
import pynyc

#Prints an actvity suitable for sunny weather
activity = pynyc.find_activity("sunny")
print(activity)
```

## `find_nightlife_activity(vibe)`

Returns one nightlife recommendation in New York City for a given vibe.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `vibe` | `str` | Yes | The nightlife vibe you want (e.g. `"dancing"`, `"singing"`, `"laughing"`, `"music and vibes"`) |

### Example usage

```python
import pynyc

# Get one random dancing recommendation
activity = pynyc.find_nightlife_activity("dancing")
print(f"Go to {activity['name']} for {activity['activity_type']}")
print(f"Website: {activity['website']}")

# Aliases also work
activity = pynyc.find_nightlife_activity("karaoke")
print(activity)

# Invalid vibes raise a helpful error instead of crashing silently
try:
    pynyc.find_nightlife_activity("quiet reading")
except ValueError as error:
    print(error)
```

Input is **case-insensitive** - `"DANCING"`, `"Dancing"`, and `"dancing"` all work the same.

See the full working example in [example.py](./example.py).

---

## `list_nightlife_places(vibe)`

Returns a list of nightlife places in New York City for a given vibe.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `vibe` | `str` | Yes | The nightlife vibe you want (e.g. `"dancing"`, `"singing"`, `"laughing"`, `"music and vibes"`) |

### Example usage

```python
import pynyc

# Get all nightlife places for a dancing vibe
places = pynyc.list_nightlife_places("dancing")
for place in places:
    print(f"{place['name']}: {place['website']}")

# Aliases also work
places = pynyc.list_nightlife_places("club")
print(places[0])

# Invalid vibes raise a helpful error instead of crashing silently
try:
    pynyc.list_nightlife_places("quiet reading")
except ValueError as error:
    print(error)
```

Input is **case-insensitive** - `"DANCING"`, `"Dancing"`, and `"dancing"` all work the same.

See the full working example in [example.py](./example.py).

---

---

## `get_cafe(time)`

Returns a recommended cafe in New York City based on the time of day.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `time` | `str` | Yes | Time of day (`"morning"`, `"afternoon"`, `"evening"`) |

### Example usage

```python
import pynyc

cafe = pynyc.get_cafe("morning")
print(f"You should check out {cafe}")
```

Input is **case-insensitive** - `"MORNING"`, `"Morning"`, and `"morning"` all work the same.

If the input is invalid, the function returns a helpful error message.

See the full working example in [example.py](./example.py).


## Setting Up for Development

### Prerequisites

- Python 3.10 or later
- [pipenv](https://pipenv.pypa.io/en/latest/) — install it with:

```bash
pip install pipenv
```

### 1. Clone the repository

```bash
git clone https://github.com/swe-students-spring2026/3-package-sea_otter.git
cd 3-package-sea_otter
```

### 2. Create the virtual environment and install dependencies

```bash
pipenv install --dev
```

### 3. Activate the virtual environment

```bash
pipenv shell
```

### 4. Run the tests

```bash
pipenv run pytest
```

All tests should pass. If they don't, check that you are using Python 3.10 or later.

### 5. Run the example program

```bash
pipenv run python example.py
```

---

## Environment Variables

This package does **not** require any environment variables or external database setup. All data is bundled with the package in the `Pynyc/data/` directory.

No `.env` file is needed.

---


