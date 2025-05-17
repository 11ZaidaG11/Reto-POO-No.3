class MenuItem():
    def __init__(self, name:str, price:float):
        self.name = name
        self.price = price

    def total_price(self):
        pass

class Beverage(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)
class Appetizer(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)
class MainCourse(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

class Order():
    def __init__(self):
        self.food = []



if __name__ == "__main__":
    menu = {
        "Beverage": [
            ("Soda", 5),
            ("Limonade", 4),
            ("MilkShake", 7)
        ],
        "Appetizer": [
            ("Soup", 12),
            ("Salad", 10),
            ("Bread", 8)
        ],
        "MainCourse": [
            ("Pizza", 15),
            ("Chicken", 18),
            ("Beef", 20),
            ("Sushi", 25)
        ]
    }
