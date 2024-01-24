# Variables and names.
# We use variables to structure code in  way that is readable.
# We assign values to output to variables


#we declare variables and assign values that will be printed out in the terminal
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#we print out the output of said variable by placing a variable inside a print statement, the double quotes in the string will print out the statement as it is. words without double quotes will output value assigned to it

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#study drills:
#car_pool_capacity is not defined means that the variable has not been declared/not been typed out and assigned a value to print out.
