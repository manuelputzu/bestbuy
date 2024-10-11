import pytest
from products import Product

# Test creating a normal product - this checks if you can create a product with valid details.
def test_create_normal_product():
    product = Product("MacBook Air M2", price=1450.0, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450.0
    assert product.quantity == 100

# Test creating a product with invalid details (like an empty name or negative price) - should raise an error.
def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):  # Expect ValueError for empty name
        Product("", price=1450.0, quantity=100)
    with pytest.raises(ValueError):  # Expect ValueError for negative price
        Product("MacBook Air M2", price=-10.0, quantity=100)

# Test that product becomes inactive when quantity hits 0 - ensures the product gets deactivated properly.
def test_product_becomes_inactive_when_zero_quantity():
    product = Product("MacBook Air M2", price=1450.0, quantity=1)
    product.buy(1)  # Should bring quantity to 0
    assert product.active is False

# d) Test product purchase - checks that buying a product reduces the quantity correctly.
def test_product_purchase_reduces_quantity():
    product = Product("MacBook Air M2", price=1450.0, quantity=10)
    product.buy(3)  # Reducing quantity by 3
    assert product.quantity == 7  # Check the new quantity

# e) Test buying more than available quantity raises an exception - to make sure we can't buy more than in stock.
def test_buying_larger_quantity_than_exists_raises_exception():
    product = Product("MacBook Air M2", price=1450.0, quantity=5)
    with pytest.raises(ValueError):  # Should raise an error if trying to buy more than available
        product.buy(10)
