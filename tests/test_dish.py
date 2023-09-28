import pytest
from lib.dish import *

# """
# Given a dish name
# We can see that the dish now exists
# And the price is n/a
# """
def test_dish_init():
    curry = Dish("Curry")
    assert curry.availability ==True
    assert curry.price == "n/a"

# """
# Given an invalid dish name
# We should throw an error
# """
def test_dish_init_name_error():
    with pytest.raises(Exception) as e:
        Dish("", "£8.99")
    assert str(e.value) == "Please enter a valid dish name"

# """
# Given an invalid price
# We should throw an error
# """
def test_dish_init_price_error():
    with pytest.raises(Exception) as e:
        Dish("curry", "8.99")
    assert str(e.value) == "Please enter a valid price"

# """
# Trying to set the price
# We should see this reflected in the self.price variable
# """
def test_dish_set_price():
    curry = Dish("curry", "£8.99")
    curry.set_price("£9.99")
    assert curry.price == "£9.99"

# """
# Trying to set an invalid price
# We should throw an error message
# """
def test_dish_set_price_error():
    curry = Dish("curry", "£8.99")
    with pytest.raises(Exception) as e:
        curry.set_price("9.99")
    assert str(e.value) == "Please enter a valid price"


# """
# Calling the unavailable() function
# We should see that the available variable is set to False
# Calling the available() function
# We should see that the available variable is set to True
# """
def test_dish_availability():
    curry = Dish("curry", "£8.99")
    curry.available()
    assert curry.availability == True
    curry.unavailable()
    assert curry.availability == False
    curry.available()
    assert curry.availability == True

# """
# Calling the format function
# We should see the name and price formatted in a menu format
# """
def test_dish_format():
    curry = Dish("curry", "£8.99")
    assert curry.format() == "curry  ~~~  £8.99" 

# ```