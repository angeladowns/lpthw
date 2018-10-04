# \t adds a tab space
tabby_cat = "\tI'm tabbed in."
# \n adds a new line
persian_cat = f"I'm split\non a {' '}line."
# \\ adds a backslash
backslash_cat = "I'm \\ a \\ {} cat.".format('chubby')

# """ or ''' accomplish the same thing, but ''' is easier to see/read, imo.
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
