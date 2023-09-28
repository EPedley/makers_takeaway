# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Takeaway                                                                                                       │ 
│                                                                                                                │
│   ==> dishes_ordered // list                                                                                   │
│   ==> order_complete // boolean                                                                                │
│                                                                                                                │
│ - menu() -> show all available dishes and prices                                                               │
│ - add(dish) -> add the user's chosen dish to the dishes-ordered list                                           │ 
│ - remove(dish) -> remove the user's chosen dish to the dishes-ordered list                                     │ 
│ - place_order -> call receipt() and call text()                                                                │ 
│ - receipt() -> print out all the user's ordered dishes and a total                                             │                  
│ - text() -> send an SMS message, e.g. "Thank you! Your order was placed and will be delivered before 18:52"    │
└─────────────────────────────────────────┬──────────────────────────────────────────────────────────────────────┘
                                          │
                                          │ owns a list of
                                          ▼
┌────────────────────────────────────────────────────────────────────────────────────┐
│ Dish(dish)                                                                         │ 
│                                                                                    │
│   ==> Dish name // string                                                          │
│   ==> Price // string                                                              │
│   ==> Availability // boolean                                                      │
│                                                                                    │
│ - set_price(price) -> sets the price of the dish                                   │
│ - available() -> sets the dish to available                                        │
│ - unavailable() -> sets the dish to unavailable                                    │
│ - format() -> returns the dish formatted, e.g. "Chicken Katsu Curry  ~~~  £8.99"   │
└────────────────────────────────────────────────────────────────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Takeaway:
    # User-facing properties:
    #   dishes_ordered // boolean
    #   order_complete // list

    def __init__(self):
        pass # No code here yet

    def menu(self):
        # Parameters:
        #   None
        # Returns:
        #   A formatted menu including the dishes and prices
        # Side-effects:
        #   None
        pass # No code here yet

    def add(self, dish):
        # Parameters:
        #   Dish name // string
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the chosen dish to the dishes_ordered list
        pass # No code here yet

    def remove(self, dish):
        # Parameters:
        #   Dish name // string
        # Returns:
        #   Nothing
        # Side-effects:
        #   Removes the chosen dish from the dishes_ordered list
        pass # No code here yet

    def summary(self)
        # Parameters:
        #   None
        # Returns:
        #   All the dishes in the dishes_ordered list
        # Side-effects:
        #   None
        pass # No code here yet   

    def place_order(self):
        # Parameters:
        #   None
        # Returns:
        #   Nothing
        # Side-effects:
        #   Calls the receipt() and text functions
        pass # No code here yet

    def receipt(self):
        # Parameters:
        #   None
        # Returns:
        #   A summary of the items ordered and a sum total
        # Side-effects:
        #   None
        pass # No code here yet

    def text(self):
        # Parameters:
        #   None
        # Returns:
        #   Sends an SMS text to the user, e.g. "Thank you! Your order was placed and will be delivered before 18:52" 
        # Side-effects:
        #   None
        pass # No code here yet


class Dish:
    # User-facing properties:
    #   name // string
    #   price // string
    #   availability // boolean

    def __init__(self, name, price(optional)):
        pass # No code here yet

    def set_price(self, price):
        # Parameters:
        #   Price // string
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the self.price variable
        pass # No code here yet

    def available(self, dish):
        # Parameters:
        #   Dish name // string
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the available variable to True
        pass # No code here yet

    def unavailable(self, dish):
        # Parameters:
        #   Dish name // string
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the available variable to False
        pass # No code here yet

    def format(self):
        # Parameters:
        #   None
        # Returns:
        #   A string of the dish and price formatted, e.g. "Chicken Katsu Curry  ~~~  £8.99" 
        # Side-effects:
        #   Sets the available variable to False
        pass # No code here yet

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python

# TAKEAWAY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
Using the menu mathod we should see all the dishes and prices listed
"""
curry = Dish("Curry", "£8.99")
pasta = Dish("Pasta", "£4.99")
takeaway = Takeaway()
takeaway.menu()  
# "MENU
# Curry  ~~~ £8.99
# Pasta  ~~~ £4.99"

"""
Adding an item to the takeaway class
We should see this reflected in the dishes_ordered list
"""
curry = Dish("Curry", "£8.99")
pasta = Dish("Pasta", "£4.99")
takeaway = Takeaway()
takeaway.add("Curry")
takeaway.dishes_ordered  # => ["Curry"]

"""
Trying to add an invalid dish
We should throw an error
"""
curry = Dish("Curry", "£8.99")
pasta = Dish("Pasta", "£4.99")
takeaway = Takeaway()
takeaway.add("Kebab") # => "Please enter a valid dish"

"""
Removing an item from the takeaway class
We should see this reflected in the dishes_ordered list
"""
curry = Dish("Curry", "£8.99")
pasta = Dish("Pasta", "£4.99")
takeaway = Takeaway()
takeaway.add("Curry")
takeaway.remove("Curry")
takeaway.dishes_ordered  # => []

"""
Trying to remove an invalid dish
We should throw an error
"""
curry = Dish("Curry", "£8.99")
pasta = Dish("Pasta", "£4.99")
takeaway = Takeaway()
takeaway.remove("Curry") # => "Please enter a valid dish"

"""
Running the summary method
We should receive all the items currently in our order
"""
curry = Dish("Curry", "£8.99")
pasta = Dish("Pasta", "£4.99")
takeaway = Takeaway()
takeaway.add("Curry")
takeaway.add("Pasta")
takeaway.summary() 
# "YOUR ORDER
# Curry  ~~~ £8.99
# Pasta  ~~~ £4.99
# TOTAL: £13.98"

"""
Placing on order
We should receive a receipt
"""
curry = Dish("Curry", "£8.99")
pasta = Dish("Pasta", "£4.99")
takeaway = Takeaway()
takeaway.add("Curry")
takeaway.add("Pasta")
takeaway.place_order() 
# "THANK YOU FOR YOUR ORDER!
# 
# YOUR ORDER
# Curry  ~~~ £8.99
# Pasta  ~~~ £4.99
# TOTAL: £13.98"



```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python

# DISH ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
Given a dish name
We can see that the dish now exists
And the price is n/a
"""
curry = Dish("Curry")
curry.availability # => True
curry.price # => "n/a"

"""
Given a dish name and a price
We can see that the dish now exists
And the price is set
"""
curry = Dish("Curry", "£8.99")
curry.availability # => True
curry.price # => "£8.99"

"""
Given an invalid dish name
We should throw an error
"""
curry = Dish("". "£8.99") # => "Please enter a valid dish name"

"""
Given an invalid price
We should throw an error
"""
curry = Dish("curry". "8.99") # => "Please enter a valid price"

"""
Calling the unavailable() function
We should see that the available variable is set to False
Calling the available() function
We should see that the available variable is set to True
"""
curry = Dish("curry". "8.99")
curry.available()
curry.availability # => True
curry.unavailable()
curry.availability # => False

"""
Calling the format function
We should see the name and price formatted in a menu format
"""
curry = Dish("curry". "8.99") # => "Please enter a valid price"
curry.format() => "curry  ~~~  £8.99" 


```python

# TAKEAWAY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
Creating an instance of the Takeaway class
We should see an empty list and the Order Complete variable set to False
"""
takeaway = Takeaway()
takeaway.dishes_ordered = []
takeaway.order_complete = False

"""
Using the menu mathod we should see all the dishes and prices listed
"""
curry = Dish("Curry", "£8.99")
pasta = Dish("Pasta", "£4.99")
takeaway = Takeaway()
takeaway.menu()  
# "MENU
# Curry  ~~~ £8.99
# Pasta  ~~~ £4.99"

"""
Adding an item to the takeaway class
We should see this reflected in the dishes_ordered list
"""
curry = Dish("Curry", "£8.99")
pasta = Dish("Pasta", "£4.99")
takeaway = Takeaway()
takeaway.add("Curry")
takeaway.dishes_ordered  # => ["Curry"]

"""
Trying to add an invalid dish
We should throw an error
"""
curry = Dish("Curry", "£8.99")
pasta = Dish("Pasta", "£4.99")
takeaway = Takeaway()
takeaway.add("Kebab") # => "Please enter a valid dish"

"""
Removing an item from the takeaway class
We should see this reflected in the dishes_ordered list
"""
curry = Dish("Curry", "£8.99")
pasta = Dish("Pasta", "£4.99")
takeaway = Takeaway()
takeaway.add("Curry")
takeaway.remove("Curry")
takeaway.dishes_ordered  # => []

"""
Trying to remove an invalid dish
We should throw an error
"""
curry = Dish("Curry", "£8.99")
pasta = Dish("Pasta", "£4.99")
takeaway = Takeaway()
takeaway.remove("Curry") # => "Please enter a valid dish"

"""
Running the summary method
We should receive all the items currently in our order
"""
curry = Dish("Curry", "£8.99")
pasta = Dish("Pasta", "£4.99")
takeaway = Takeaway()
takeaway.add("Curry")
takeaway.add("Pasta")
takeaway.summary() 
# "YOUR ORDER
# Curry  ~~~ £8.99
# Pasta  ~~~ £4.99
# TOTAL: £13.98"

"""
Placing on order
We should receive a receipt
"""
curry = Dish("Curry", "£8.99")
pasta = Dish("Pasta", "£4.99")
takeaway = Takeaway()
takeaway.add("Curry")
takeaway.add("Pasta")
takeaway.place_order() 
# "THANK YOU FOR YOUR ORDER!
# 
# YOUR ORDER
# Curry  ~~~ £8.99
# Pasta  ~~~ £4.99
# TOTAL: £13.98"


```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->