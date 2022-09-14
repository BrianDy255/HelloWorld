import csv


class Item:
    pay_rate = 0.8 #The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price:float, quantity:int):
        #run validatiosn to the received arguments
        assert price >= 0, f'Price {price} is not greater than zero!'
        assert quantity >= 0, f'Quantitiy {quantity} is not greater than zero!'

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f'An instance created: {name}')

        # Actions to execute
        Item.all.append(self)   #creates a list of the objects that are created

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        print(f'Normal Price: {self.price}')
        self.price = self.price * self.pay_rate
        return f'Discounted Price: {self.price}'

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )
    @staticmethod
    def is_integer(num):
        #We will count out the floats that are point zero
        #for examplke i.e.: 5.0, 10.0
        if isinstance(num, float):
            #Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):     #__repr__ stands for represent. A useful way to unpack a list
        return f"Item('{self.name}', '{self.price}', {self.quantity}"

print(Item.is_integer(3.1))