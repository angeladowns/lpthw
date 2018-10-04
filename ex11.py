print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# FYI: end=' ' tells print to not end the line with a newline character and go to the next line.

# Random examples I found on the internets
name = input("What's your name? ")
print("Nice to meet you " + name + "!")
age = input("Your age? ")
print("So, you are already " + str(age) + " years old, " + name + "!")

# Study Drill - Write another form to ask questions...
print("Kiki, do you love me?", end=' ')
feelings = input()
print("Are you riding?", end=' ')
riding = input()
print('''
Say you'll never ever leave from beside me
'Cause I want ya, and I need ya
And I'm down for you always
'''
)
print(f"It sounds like {feelings}, you love me and {riding}, you are riding. That's great to hear!")
