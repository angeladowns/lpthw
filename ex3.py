# + plus does addition
# - minus does substraction
# / slash does division
# * asterisk does multiplication
# % percent returns the remainder after division (modulus operator)
# < less-than compares values and returns True or False
# > greater-than compares values and returns True or False
# <= less-than-equal compares values less than or equal and returns True or False
# >= greater-than-equal compares values greater or equal and returns True or False

# This prints a string.
print("I will now count my chickens:")

# This prints a string and adds 25 and 30 and then divides it by 6
print("Hens", 25.0 + 30.0 / 6.0)
# This prints a string and then multiplies 25 times 3, then it finds the remainder of 75 divided by 4, the answer is 3. Then it subtracts 3 from 100. The final answer is 97.
print("Roosters", 100.0 - 25.0 * 3.0 % 4.0)

# This prints a string.
print("Now I will count the eggs:")

# This divides 1 by 4 to get 0.25. Then it divides 4 by 2 to get a remainder of 0. Then it adds 3, 2, 1, subtracts 5, subtracts 0.25, and adds 6 to get a final answer of 6.75. Odd number for eggs.
print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)

# This prints a string.
print("Is it true that 3 + 2 < 5 - 7?")

# This adds 3 and 2 and subtracts 7 from 5 and then determines if 5 is less than negative 2. Nope. This is False.
print(3.0 + 2.0 < 5.0 - 7.0)

# This prints a string followed by the number 5.
print("What is 3 + 2?", 3.0 + 2.0)
# This prints a string followed by the number negative 2.
print("What is 5 - 7?", 5.0 - 7.0)

# This prints a string.
print("Oh, that's why it's False.")

# This prints a string.
print("How about some more.")

# This prints a string followed by True because 5 is greater than negative 2.
print("Is it greater?", 5.0 > -2.0)
# This prints a string followed by True because 5 is greater than or equal to negative 2.
print("Is it greater or equal?", 5.0 >= -2.0)
# This prints a string followed by False because 5 is not less than or equal to neagive two.
print("Is it less or equal?", 5.0 <= -2.0)
