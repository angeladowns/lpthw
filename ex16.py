from sys import argv

script, filename = argv

print(f"We are going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I am going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# STUDY DRILL - Take the six lines above and combine them.
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# ALWAYS CLOSE - To avoid leakage. What??
print("And finally we close it.")
target.close()

print("Open the file in read mode.")
target = open(filename, 'r')
print("Read the file... ")
print(target.read())
print("And close the file... Boom!")
target.close()
