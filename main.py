# Silent Auction Program

from art import logo
# Display the ASCII art for logo.
print(logo)

# Function to find which bidder won.
def greatest_bidder(bidding_record):
    # Variable to store highest bid value.
    highest_bid = 0
    # Variable to store name of the bidder who won.
    winner = ""
    # Traversing the dictionary: bidding_record
    for bidder in bidding_record:
        # Here, key = bidder, value = bidding_record[bidder]
        # Hence we store the money a bidder bid in the variable 'price'.
        price = bidding_record[bidder]
        # If the price is greater than current highet_bid value,
        # store the price in highest_bid, and name of the bidder in winner.
        if price > highest_bid:
            highest_bid = price
            winner = bidder

    # Output who won.
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

# Creating an empty dictionary to store the key: value pairs, which are name(of bidder): price they bid.
bidders = {}
end_of_bidding = False
print("\nWelcome to the secret auction program.")

# Continue bidding until end_of_bidding = True.
while not end_of_bidding == True:
    # Take input.
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))

    # Adding key: value pairs in the dictionary.
    bidders[name] = bid

    # Continue bidding if user types "yes",
    more_bidders = input('Are there any other bidders? Type "yes" or "no": ')
    # Else end the bidding and declare who won.
    if more_bidders == "no":
        end_of_bidding = True
        # Passing 'bidders' dictionary as argument to the function to find which bidder won.
        greatest_bidder(bidders)
