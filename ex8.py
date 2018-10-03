# formatter is a variable that equals four empty curly brackets that can be used to pass other data
formatter = "{} {} {} {}"

# this prints the formatter variable with 1, 2, 3, 4 in places of the curly brackets
print(formatter.format(1, 2, 3, 4))
# this prints the formatter variable with one, two, three, four in place of the curly brackets
print(formatter.format("one", "two", "three", "four"))
# this prints the formatter variable with True and False
print(formatter.format(True, False, False, True))
# this prints the formatter variable wth the variable, why??
print(formatter.format(formatter, formatter, formatter, formatter))
# this prints the variable with each string replacing a curly bracket
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
