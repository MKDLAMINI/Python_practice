# Escape sequences
# here we use \t in the beginning of a string to tab out the string
tabby_cat = "\tI'm tabbed in."

# here we use a \n to create a new line between the string
persian_cat = "I'm split\non a line."

# here we add an additional backslash \ to output a backslash on the string
backslash_cat = "I'm \\ a \\ cat."

# here we adding multiple new lines \n as well as a tab \t
lets_experiment = "\nwe\nneed\tto\ntalk"

# we use a \ before the double quote and after to output a double quote within a string
response = "no we are \"over\"\n"

print(lets_experiment)
print(response)

fat_cat = """
I'll do a list:
\t* cat food
\t* fish
\t* catnip\n\t* grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

double_quote = "I am 6'2\" tall."
single_quote = 'I am 6\'2" tall.'

print(double_quote)
print(single_quote)
