
# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

def coin_flips(n):
    # Write code here
    if n <= 0:
        return 0
    else:
        flip = choice(["H", "T"])
        if flip == "H":
            return 1 + coin_flips(n-1)
        else:
            return 0 + coin_flips(n-2)

    pass

print(coin_flips(2)) 
# => ["HH", "HT", "TH", "TT"]