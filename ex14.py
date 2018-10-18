from sys import argv

# script is the file name, obvs and user_name is entered on the command line
script, user_name, snack = argv
# by creating a prompt variable, we can use it over and over without retyping it AND if we want to change it to something less kitty-like, we only have to change it once. Boom!
prompt = '>.< meowwwkay? '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)

# this forces the age to be an integer.
print(f"How old are you, {user_name}?")
age = int(input(prompt))

# using an input (age) in a print statement.
print(f"You're {age}? What kind of computer do you have?")
computer = input(prompt)

print("Are you hungry?")
hungry = input(prompt)
print(f"Looks like you're having {snack} for lunch.")

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice!
""")
