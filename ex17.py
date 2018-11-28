from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}.")

# We could do these two on one line, but how?
# this open command does not include the `w` because we are just reading
# in_file = open(from_file)
# repr gives the representation/raw python version of that thing
# print(">>>> in_file=", repr(in_file)) # for debugging
# indata = in_file.read()
indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

# "exists" will return True if a file exists, based on its name in a string as an argument. It returns False if not.
print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
# commenting out this line because we got rid of in_file
# in_file.close()
