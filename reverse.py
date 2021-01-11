# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse(ss):
    # Write code here
    if len(ss) < 2:
        return ss
    else:
        mid = len(ss)//2 #rounds results down to the nearest whole number
        return reverse(ss[mid:]) + reverse(ss[:mid])
    pass

#solution 2

def reverse2(input, already_reversed = ''):
    if len(input) == 0:
        return already_reversed
    new_already_reversed = input[0] + already_reversed
    new_input = input[1:]
    
    return reverse2(new_input, new_already_reversed)



print(reverse("")) 
print(reverse2(""))
# => ""
print(reverse("a")) 
# => "a"
print(reverse("ab")) 
# => "ba"
print(reverse("computer")) 
print(reverse2("computer"))
# => "retupmoc"
print(reverse(reverse("computer"))) 
# => "computer"