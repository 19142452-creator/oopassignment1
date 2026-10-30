import pytest

from inventory import Inventory
from product import Product


def make():
    return Product("Milk", "MLK001", 1.25, 12)


def test_negative_price_raises_value_error():
    with pytest.raises(ValueError):
        Product("Milk", "MLK001", -1, 5)


def test_non_number_price_raises_type_error():
    with pytest.raises(TypeError):
        Product("Milk", "MLK001", "cheap", 5)


def test_quantity_rules():
    with pytest.raises(ValueError):
        Product("Milk", "MLK001", 1.0, -3)
    with pytest.raises(TypeError):
        Product("Milk", "MLK001", 1.0, 2.5)


def test_computed_properties_are_read_only():
    p = make()
    assert p.line_value == pytest.approx(15.0)
    assert p.is_low_stock is False
    with pytest.raises(AttributeError):
        p.line_value = 1


def test_low_stock():
    assert Product("Tea", "TEA009", 2.0, 4).is_low_stock is True


def test_sku_validation():
    assert Product.is_valid_sku("MLK001")
    assert not Product.is_valid_sku("ML001")
    assert not Product.is_valid_sku("MLK0012")
    with pytest.raises(ValueError):
        Product("X", "bad", 1.0, 1)


def test_from_csv_line_and_repr():
    p = Product.from_csv_line("Milk,MLK001,1.25,12")
    assert repr(p) == "Product('Milk', 'MLK001', 1.25, 12)"


def test_count_ignores_invalid_products():
    before = Product.count()
    make()
    with pytest.raises(ValueError):
        Product("X", "MLK001", -1, 1)
    assert Product.count() == before + 1


def test_inventory_operations():
    inv = Inventory.from_lines(["Milk,MLK001,1.25,12", "Eggs,EGG003,2.40,30"])
    assert inv.total_value() == pytest.approx(87.0)
    assert inv.find("MLK001").name == "Milk"
    assert inv.find("ZZZ999") is None
    inv.remove("MLK001")
    assert len(inv) == 1
    with pytest.raises(KeyError):
        inv.remove("MLK001")