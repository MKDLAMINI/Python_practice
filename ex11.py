# Asking questions

# we create a question that'll will be prompted to the user, we use end= ' ' not to end the string in a newline
print("How old are you?", end=' ')
# we then assign input function to the age variable to ask the user to input their age 
age = input()
print("How tall are you?", end= ' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print("Do you like apples? (yes/no): ", end= ' ')
answer = input()

# we use an f string to store and output the input of the user
print(f"So, you're {age} old, {height} tall and {weight} heavy and {answer} apples.")
