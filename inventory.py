"""Inventory class for the MiniMart inventory system."""

from product import Product


class Inventory:
    """A collection of products keyed by SKU."""

    def __init__(self):
        self._products = {}  # per-instance data, created in __init__

    def add(self, product):
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added")
        if product.sku in self._products:
            raise ValueError(f"SKU {product.sku} already exists")
        self._products[product.sku] = product

    def remove(self, sku):
        """Remove and return the product; KeyError if missing."""
        try:
            return self._products.pop(sku)
        except KeyError:
            raise KeyError(f"No product with SKU {sku}") from None

    def find(self, sku):
        """Return the product, or None if the SKU is unknown."""
        return self._products.get(sku)

    def total_value(self):
        return sum(p.line_value for p in self._products.values())

    def low_stock(self):
        return [p for p in self._products.values() if p.is_low_stock]

    def __iter__(self):
        return iter(self._products.values())

    def __len__(self):
        return len(self._products)

    @classmethod
    def from_lines(cls, lines):
        """Build a complete inventory from CSV lines."""
        inventory = cls()
        for line in lines:
            inventory.add(Product.from_csv_line(line))
        return inventory