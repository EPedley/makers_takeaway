class Dish:

    def __init__(self, name, price="n/a"):
        if type(name) is not str or len(name) == 0:
            raise Exception("Please enter a valid dish name")
        elif self.check_price(price) is False and price != "n/a":
            raise Exception("Please enter a valid price")
        else:
            self.name = name
            self.price = price
            self.availability = True

    def check_price(self, price):
        if price[0] == "£":
            return True
        return False

    def set_price(self, price):
        if self.check_price(price):
            self.price = price
        else:
            raise Exception("Please enter a valid price")

    def available(self):
        self.availability = True

    def unavailable(self):
        self.availability = False

    def format(self):
        return f"{self.name}  ~~~  {self.price}"
# 