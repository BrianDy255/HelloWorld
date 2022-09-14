#this version takes out the function for adding in dictionaries in a list as the function was not necessary
#Also uses the function to find the highest bidder using the dictionary values rather than using the methods for max() value
import art
print(art.logo)

print("Welcome to the secret auction program.")

auction_dictionary = {}
end_program = True

def highest_bidder(bidding_record):
    highest_bidder_value = 0
    highest_bidder_name = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bidder_value:
            highest_bidder_value = bid_amount
            highest_bidder_name = bidder
    print(f"The highest bidder is {highest_bidder_name} with a winning bid of ${highest_bidder_value}")

while end_program != False:
    user_name = input("What is your name?\t").title()
    user_bid = int(input("What's your bid? $"))
    #Adds items to the dictionary. Original version had the dictionary in a list, which was not necessary
    auction_dictionary[user_name] = user_bid
    cont_program = input("Are there any other bidders? Type 'Yes' or 'No'\n")
    highest_bidder(auction_dictionary)
    if cont_program == "no":
        end_program = False