print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill?"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))


final_price = (total / people) * (tip/100)
results = total/people + final_price
print(f'${round(results,2)}')