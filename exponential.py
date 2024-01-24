# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.

# pseudocode

# create a function called exponent 
def exponent (base, exp):

# calculate the result when the base is raise to exp
    result = base ** exp

# conditions
   # check if the exp is equal to 0
    if exp == 0:
        print (f"{base} raises to the power of {exp}: 1")

   # check if the exp is less than 0
    elif exp < 0:
        print ("Exponent cannot be a negative integer.")

    else:
        print (f"{base} raises to the power of {exp}: {result}")

# print the result
exponent (20,0)
exponent (10,-2)
exponent (3,7)