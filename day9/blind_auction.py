import auction_art

print(auction_art.gavel)
print("Welcome to the secret auction program")

bidding = {}

def find_winner(dictionary):
    highest_bid = 0
    winner = ""
    for key in dictionary:
        if dictionary[key] > highest_bid:
            highest_bid = dictionary[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}")

over = False
while not over:
    name = input("What's your name: ")
    price = int(input("What's your bid price: $"))
    bidding[name] = price

    another_bid = input("Is there any other bidders? 'yes' or 'no': ")
    if another_bid == "no":
        is_over = True
        find_winner(bidding)