sandwich_orders = ['pastrami', 'veggie', 'chicken', 'pastrami', 'turkey', 'pastrami',]

finished_sandwich = []

print("We have currently run out of Pastrami Sandwiches =(")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    orders = sandwich_orders.pop()
    print(f"Currently working on {orders}")
    finished_sandwich.append(orders)

for sandwich in finished_sandwich:
    print(f"Your {sandwich} is ready for pickup")
