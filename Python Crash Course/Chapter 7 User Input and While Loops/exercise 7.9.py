sandwich = ['pastrami', 'veggie', 'grilled cheese', 'pastrami', 'turkey',
            'roast beef', 'pastrami']

finished_sandwiches = []

print("I'm sorry we're all out of pastrami")
while 'pastrami' in sandwich:
    sandwich.remove('pastrami')

while sandwich:
    ordered_sandwich = sandwich.pop()
    print(f"I'm currently working on {ordered_sandwich} sandwich")
    finished_sandwiches.append(ordered_sandwich)


for sandwich in finished_sandwiches:
    print(f"Your {sandwich} are ready!")