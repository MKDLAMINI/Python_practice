# Strings and Text
# The interpreter registers a string when we put "" or '' around text.

# We declare a variable and assign data to print 
types_of_people = 10

# interesting...we declare a variable that contains an f-string, that f-string will output data from a prev declared variable
x = f"There are {types_of_people} types of people."

# variable declaration assigning strings to print
binary = "binary"
do_not = "don't"

y = f"Those who know {binary} and those who {do_not}."

# we print out the values contained in x and y
print(x)
print(y)

# we print out the values of x and y using an f-string
print(f"I said: {x}\nI also said: '{y}'")

# assign data to variables 
hilarious = False

# we assign a string with {} that serves as a placeholder for 'hilarious'
joke_evaluation = "Isn't that joke so funny?! {}"

# we use .format(declared_variable) to print out the info assigned to it
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
