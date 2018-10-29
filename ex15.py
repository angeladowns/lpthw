from sys import argv
# we need to type in the script name and the filename in the command line to run the script. ex python3.6 ex15.py ex15_sample.txt
script, filename = argv
# txt is a variable that we have set to open the filename entered in the command line - just open, nothing else
txt = open(filename)

print(f"Here's your file {filename}:")
# this is where we tell python to READ the file the txt variable opened
print(txt.read())

print("Type the filename again:")
# now we are prompting the user to enter the filename using input()
file_again = input('> ')
# just like line 5, we are telling Python to open the above mentioned filename
txt_again = open(file_again)
# just like line 9, we are telling Python to read the open file
print(txt_again.read())

txt.close()
txt_again.close()
