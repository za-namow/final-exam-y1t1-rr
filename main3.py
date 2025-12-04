class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"Hi, I'm {self.name}")

class Customer(Person):
    def __init__(self, address):
        self.address = address
    def place_order(item):
        return DeliveryOrder.item

class Driver(Person):
    def __init__(self, vehicle):
        self.vehicle = vehicle
    def deliver(order):
            print(f'{Person.name} is delivering {order.item} to {Person.name} using {order.vehicle}')

class DeliveryOrder:
    def __init__(self, customer, item, status="preparing"):
        self.customer = customer
        self.item = item
        self.status = status
    def assign_driver(driver):
        pass
    def summary():
        return f"Order for {DeliveryOrder.order} → {DeliveryOrder.status}"

if __name__ == "__main__":
    name = Person("Alice")
    name.introduce()