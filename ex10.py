tabby_cat = "\tI'm tabbed in."
persian_cat = "Im split\non a line."
backslash_cat = "I'm \\ a \\ cat."

#there is no list function at work here, it's just a """" being used to allow text to travel across multiple lines
#the * is part of the text anf the /t adds a tab AKA indent
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)