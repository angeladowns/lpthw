# this defines the function; cheese_count and boxes_of_crackers are the variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # debugging
    print(">>>> cheese_count =", cheese_count)
    print(">>>> boxes_of_crackers = ", boxes_of_crackers)
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")
    print(">>>> exit cheese_and_crackers debugging.\n\n")

# this will print the statement below and then it will call the function and assign 20 to cheese_count and 30 to boxes_of_crackers
print("We can just give the functions numbers directly:")
cheese_and_crackers(20, 30)

# this will print the statement below and then it will temporarily assign 10 to cheese_count and 50 to boxes_of_crackers
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# this will print the function using the variables created above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# this will print the function with 30 cheeses and 11 boxes
print("We can even do math inside, too:")
cheese_and_crackers(10 + 20, 5 + 6)

# this will add 100 to the variable for cheese and 1000 to the variable for crackers
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# this is interesting. So, I created a bunch of variables and then I add them up when I call the function. I imagine it may be useful for adding up the number of adventures in predefined categories or cites?
print("Can we add variables?")
cheddar = 10
american = 20
provolone = 30
wheat_crackers = 40
sesame_crackers = 90
water_crackers = 500

cheese_and_crackers(cheddar + american + provolone + 10, wheat_crackers + sesame_crackers + water_crackers + 10)
