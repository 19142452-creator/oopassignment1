"""Demonstration script for the MiniMart inventory system."""

from inventory import Inventory
from product import Product

SAMPLE = [
    "Milk,MLK001,1.25,12",
    "Bread,BRD002,0.90,3",
    "Eggs,EGG003,2.40,30",
    "Coffee,COF004,7.50,2",
]


def print_report(inventory):
    print("MiniMart Inventory Report")
    print("=" * 45)
    for p in inventory:
        print(
            f"{p.name:<10} {p.sku:<8} "
            f"{p.price:>6.2f} x {p.quantity:>3} = {p.line_value:>8.2f}"
        )
    print("-" * 45)
    print(f"Total inventory value: {inventory.total_value():.2f}")
    print()
    print("Low-stock items:")
    for p in inventory.low_stock():
        print(f"  - {p.name} ({p.sku}): only {p.quantity} left")


def main():
    inventory = Inventory.from_lines(SAMPLE)
    print_report(inventory)
    print(f"\nProducts created: {Product.count()}")


if __name__ == "__main__":
    main()