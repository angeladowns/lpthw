from sys import argv
# read the What You Should See section for how to run this
# assigning variables to argv
script, first, second, third = argv
# answers the question "What is argv?"
print(">>>> argv=", repr(argv))

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your second third variable is:", third)
# using input() to prompt for data
name = input("What's your name? ")
