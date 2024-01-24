# More variables and names

# We are going to be using format strings also known as f strings. We use f strings to store variables within strings inside curly braces {}
name = 'MK Dlamini'
age = 26
height = 70 #inches
weight = 100 #lbs
height_in_cm = height * 2.54
weight_in_kg = weight / 2.2046
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_in_cm} inches tall.")
print(f"He's {weight_in_kg} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height_in_cm + weight_in_kg
print(f"If I add {age}, {height_in_cm}, and {weight_in_kg} I get {total}.")
