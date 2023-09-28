from dish import *
from twilio.rest import Client
from datetime import datetime, timedelta
from config import *

class Takeaway:

    def __init__(self, client=None):
        self.dishes_ordered = []
        self.order_complete = False
        if not client:
            self.client = Client(account_sid, auth_token)
        else:
            self.client = client

    def menu(self):
        return "MENU\n" + "\n".join([dish.format() for dish in self.dishes_ordered])

    def add(self, dish):
        if not isinstance(dish, Dish):
            raise Exception("Please enter a valid dish")
        self.dishes_ordered.append(dish)

    def remove(self, dish):
        if not isinstance(dish, Dish):
            raise Exception("Please enter a valid dish")
        elif dish not in self.dishes_ordered:
            raise Exception("You haven't added that dish to your order")
        else:
            self.dishes_ordered.remove(dish)

    def summary(self):
        total = sum([float(dish.price[1:]) for dish in self.dishes_ordered])
        return "YOUR ORDER\n" + "\n".join([dish.format() for dish in self.dishes_ordered]) + "\nTOTAL: £" + str(total)

    def place_order(self):
        self.order_complete = True
        self.text()
        return "THANK YOU FOR YOUR ORDER!\n\n" + self.summary()
        
    def text(self, body="Thank you! Your order was placed"):
        delivery_time = len(self.dishes_ordered) * 5 + 10        
        estimated_order_arrival_time = (datetime.now() + timedelta(minutes = delivery_time)).strftime("%H:%M")
        body += f" and will be delivered before {estimated_order_arrival_time}."

        message = self.client.messages.create(
            to="+447704904483", 
            from_="+447700156940",
            body=body)

        return message.sid
    