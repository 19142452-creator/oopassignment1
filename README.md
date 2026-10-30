# MiniMart Inventory (OOP Assignment 1)

A small object-oriented program that keeps track of the products
MiniMart stocks: name, SKU, unit price and quantity on hand.

## How to run

Requires Python 3.10+ (standard library only).

    python main.py

To run the optional tests:

    pip install pytest
    pytest

## Files

- `product.py` - the `Product` class
- `inventory.py` - the `Inventory` class
- `main.py` - demonstration script that prints the report
- `test_product.py` - pytest tests (bonus)

## Design decisions

- **Validation in setters:** `__init__` assigns `price` and `quantity`
  through their property setters, so an invalid `Product` can never exist,
  even if the values are changed later. `bool` is rejected as a number.
- **SKU validation:** `is_valid_sku` is a staticmethod because it needs
  neither the class nor an instance. `__init__` uses it and raises
  `ValueError` for a bad SKU.
- **Product counter:** `_count` is a class attribute increased at the end
  of `__init__`, so failed constructions are not counted. All per-instance
  data (including the inventory dictionary) is created in `__init__`.
- **Factories:** `from_csv_line` and `from_lines` are classmethods, so
  they also work with subclasses.
- **Inventory behaviour:** `add` rejects a duplicate SKU, `remove` raises
  `KeyError` for an unknown SKU, and `find` returns `None` if not found.
- **Computed properties:** `line_value` and `is_low_stock` are read-only
  properties, so they are always consistent with price and quantity.