# This prints a simple string.
print("Mary had a little lamb.")
# This prints a string and formats the empty bracket.
# snow is not a variable, it is just a string.
print("Its fleece was white as {}.".format('snow'))
# This prints a simple string.
print("And everywhere that Mary went.")
# This prints a period ten times.
print("boing" * 10) # what'd that do? My guess is ten periods.

# Lines 11 - 22 assign letters to variables.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens -- it causes a syntax error
# this prints Cheese with a space at the end
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# this prints Burger. I'm hungry.
print(end7 + end8 + end9 + end10 + end11 + end12)
