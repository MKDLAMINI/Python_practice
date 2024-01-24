# Printing printing
# we declare the variable format and assign {} into a string
formatter = "{} {} {} {}"

# we use .format to print the data of the formatter variable, palceholder {} must the number of data in order to print.
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(
    "Nothing like",
    "Good old sunday",
    "Practice and some Kendo",
    "And maybe bake something",
))
