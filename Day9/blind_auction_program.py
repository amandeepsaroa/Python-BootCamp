from art import logo
import os

def find_max_bid(bids):
    
    max_bid = 0
    max_bidding_person = ""
    for i in range(len(bids)):
        
        current_bid = bids[i]["Bid Amount"]
        current_bidding_person = bids[i]["Name"]

        if current_bid > max_bid:

            max_bid = current_bid
            max_bidding_person = current_bidding_person
    
    return max_bidding_person , max_bid


print(logo)
print("Welcome to the secret auction program.")
bids = []
bid_state = 'yes'

while bid_state == 'yes':

    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    bid_state = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    
    bids.append({"Name": name , "Bid Amount": bid_amount})
    if bid_state.lower() == 'no':
        os.system('cls')
        break

    os.system('cls')

final_winner_name , max_bid = find_max_bid(bids)
print(f"The winner is {final_winner_name} with a bid of ${max_bid}")

