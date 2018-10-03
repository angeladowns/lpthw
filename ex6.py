types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary" # this is a string
do_not = "don't"  # this is a string
# this is a string inside a string... twice.
y = f"Those who know {binary} and those who {do_not}." # removed `f` to cause a break
print(">>>> after assign y", y)

print(x)
print(y)

# this is a string inside a string inside another string
print(f"I said: {x}")
# this is a string inside a string inside another string
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# I don't understand how this is formatted by False
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# Using the + sign links two strings
print(w + e)
