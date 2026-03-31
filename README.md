# Python Package Exercise

[![log github events](https://github.com/swe-students-spring2026/3-package-sea_otter/actions/workflows/event-logger.yml/badge.svg?branch=main&event=workflow_run)](https://github.com/swe-students-spring2026/3-package-sea_otter/actions/workflows/event-logger.yml)

## Github

[Link](https://github.com/swe-students-spring2026/3-package-sea_otter)

## Developers

[Albert Chen](https://github.com/azc9673)
[Blake Chang](https://github.com/louisvcarpet)
[Valeria Chang](https://github.com/ValeriaChang)
[Vincent Campanaro](https://github.com/vincentcamp)

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

# Get any Italian restaurant
restaurant = pynyc.find_restaurant("italian")
print(f"Go to {restaurant}")

# Get a Michelin-listed Japanese restaurant
restaurant = pynyc.find_restaurant("japanese", michelin=True)
print(f"Go to {restaurant}")

# Invalid cuisine returns a helpful message instead of crashing
result = pynyc.find_restaurant("klingon")
print(result)
# Google and ask it to generate one restaurant for this cuisine, we don't have a great choice of this yet oops.
```

Input is **case-insensitive** — `"ITALIAN"`, `"Italian"`, and `"italian"` all work the same.

See the full working example in [example.py](./example.py).

---

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

This package does **not** require any environment variables or external database setup. All restaurant and activity data is bundled with the package in the `Pynyc/data/` directory.

No `.env` file is needed.

---

## Team

| Name | GitHub |
|---|---|
| Albert Chen | [@azc9673](https://github.com/azc9673) |
| Blake Chang | [@louisvcarpet](https://github.com/louisvcarpet) |
| Valeria Chang | [@ValeriaChang](https://github.com/ValeriaChang) |
| Vincent Camp | [@vincentcamp](https://github.com/vincentcamp) |
