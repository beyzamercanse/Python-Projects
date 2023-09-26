from replit import clear
# HINT: You can call clear() to clear the output in the console.

# from art import logo
# print(logo)

bids = {}
bids_finished = False


# find the highest value in dictionary (just like in list)
def find_highest_bid(bids):

    highest_bid = 0
    winner = " "

    for bidder_person in bids:  # bidder is key nt value or   key, value
        bid_amount = bids[bidder_person]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder_person
    print(f"the winner is {winner} with the bid of ${highest_bid}")


while not bids_finished:

    name = input("what is yur name? ")
    price = int(input("what is your bid? "))
    bids[name] = price
    answer = input("are there any other bidders? type 'yes' or 'no'.")
    if answer == "yes":
        clear()
    else:
        bids_finished = True
        find_highest_bid(bids)


# command + ] for multi-shift space
