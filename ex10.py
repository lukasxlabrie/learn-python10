#these are all VAR but with a variety of new functions
#\t adds a tab
tabby_cat = "\tI'm tabbed in."
persian_cat = "Im split\non a line." #\n starts a new line
backslash_cat = "I'm \\ a \\ cat." #this adds a \ between defined areas

#there is no list function at work here, it's just a """" being used to allow text to travel across multiple lines
#the * is part of the text anf the /t adds a tab AKA indent
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
#these are just telling the program what to show in the output
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)