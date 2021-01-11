
# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

def coin_flips(n):
    # Write code here
    if n == 1:
        return ["H", "T"]
    
    already_flipped = coin_flips(n - 1)
    
    history_plus_heads = list(map(lambda el: el + "H", already_flipped))
    history_plus_tails = list(map(lambda el: el + "T", already_flipped))
    
    return history_plus_heads + history_plus_tails

  

print(coin_flips(2)) 
# => ["HH", "HT", "TH", "TT"]