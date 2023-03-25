from day_Blind_auction_art import logo

print(logo)
print("Welcome to secret auction program")

bids = {}
willBeBets = 'Y'
finish_bidding = False

while not finish_bidding:
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    bids[name] = int(bid)
    willBeBets = input("Are there any other bidders? Type 'Y' or 'N' ")
    if willBeBets == "Y":
        continue
    else:
        finish_bidding = True

max_bid = 0
for name in bids.keys():
    if max_bid < bids[name]:
        max_bid = bids[name]

print(bids)
print(f"Max bid is {max_bid}")

# bids = []
# willBeBets = 'Y'
#
# while willBeBets == 'Y':
#     name = input("What is your name?: ")
#     bid = input("What's your bid?: $")
#     bids.append({
#         "name": name,
#         "bid": int(bid)
#     })
#     willBeBets = input("Are there any other bidders? Type 'Y' or 'N' ")
#
# max_bid = 0
# for bid in bids:
#     if max_bid < bid["bid"]:
#         max_bid = bid["bid"]
#
# print(bids)
# print(f"Max bid is {max_bid}")

