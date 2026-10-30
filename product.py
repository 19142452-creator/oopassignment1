"""Product class for the MiniMart inventory system."""

import re


class Product:
    """A product with a name, SKU, unit price and quantity on hand."""

    LOW_STOCK_THRESHOLD = 5
    _SKU_PATTERN = re.compile(r"[A-Za-z]{3}\d{3}")
    _count = 0  # shared by all products: how many have been created

    def __init__(self, name, sku, price, quantity):
        if not self.is_valid_sku(sku):
            raise ValueError(
                f"Invalid SKU {sku!r}: expected 3 letters then 3 digits"
            )
        self.name = name
        self.sku = sku
        self.price = price        # goes through the property setter
        self.quantity = quantity  # goes through the property setter
        Product._count += 1       # only counted if validation succeeded

    # ---------- properties ----------
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("price must be a number")
        if value < 0:
            raise ValueError("price cannot be negative")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("quantity must be an integer")
        if value < 0:
            raise ValueError("quantity cannot be negative")
        self._quantity = value

    @property
    def line_value(self):
        """Read-only: price x quantity."""
        return self.price * self.quantity

    @property
    def is_low_stock(self):
        """Read-only: True when quantity is below the threshold (5)."""
        return self.quantity < self.LOW_STOCK_THRESHOLD

    # ---------- class tools ----------
    @classmethod
    def from_csv_line(cls, line):
        """Build a Product from 'name,sku,price,quantity'."""
        parts = [part.strip() for part in line.split(",")]
        if len(parts) != 4:
            raise ValueError(f"Expected 4 comma-separated fields: {line!r}")
        name, sku, price, quantity = parts
        return cls(name, sku, float(price), int(quantity))

    @staticmethod
    def is_valid_sku(sku):
        """True only for three letters followed by three digits."""
        return isinstance(sku, str) and bool(
            Product._SKU_PATTERN.fullmatch(sku)
        )

    @classmethod
    def count(cls):
        """Number of Product objects created so far."""
        return Product._count

    def __repr__(self):
        return (
            f"Product({self.name!r}, {self.sku!r}, "
            f"{self.price!r}, {self.quantity!r})"
        )