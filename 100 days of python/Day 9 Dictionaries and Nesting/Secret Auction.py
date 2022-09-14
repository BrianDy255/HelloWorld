import art
print(art.logo)

print("Welcome to the secret auction program.")

auction_list = []
auction_dictionary = {}
highest_bidder_value = 0
highest_bidder_name = ""

end_program = True

def auction_program(user_name,user_bid):
    auction_dictionary[user_name] = user_bid
    print(f"{user_name} currently bids ${user_bid}")
    auction_list.append(auction_dictionary)

while end_program != False:
    user_name = input("What is your name?\t").title()
    user_bid = int(input("What's your bid? $"))
    auction_program(user_name,user_bid)
    highest_bidder_value = max(auction_dictionary.values())
    highest_bidder_name = max(auction_dictionary, key=auction_dictionary.get)
    cont_program = input("Are there any other bidders? Type 'Yes' or 'No'\n")
    if cont_program == "no":
        end_program = False
        print(f"The highest bidder is {highest_bidder_name} with a bid of ${highest_bidder_value}")
