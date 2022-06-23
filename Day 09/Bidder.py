#from replit import clear

bid_continue = True
bidders = {}
winner = ""
bid = 0

while bid_continue:
    bidder_name = input("What's your name?")
    bid = int(input("How much ur bidding?"))
    bidders[bidder_name] = bid
    stop_bidding = input("Any other bidders? (y/n)")
    if stop_bidding == "n":
        bid_continue = False

for name in bidders:
    print(name)
    print(bidders[name])    
    if bidders[name] > bid:
        winner = name
        bid = bidders[name]
    
print(f"Congratulations! {winner} won with bid of {bid}")