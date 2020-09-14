class CoffeeCup():
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def fill(self):
        self.amount = self.capacity

    def empty(self):
        self.amount = 0
    
    def drink(self, amount):
        self.amount -= amount
        if (self.amount == 0):
            self.amount = 0
            print("Coffee cup is now empty")