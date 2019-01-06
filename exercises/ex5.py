# More Variables and Printing

def cm_to_inch(n):
    return n * 0.393701


def inch_to_cm(n):
    return n * 2.54

def kg_to_pound(n):
    return n * 2.20462

def pound_to_kg(n):
    return n * 0.453592


name = 'Du Liqiang'
age = 29
height = 172  # centimeters
weight = 120  # kilograms
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height} centimeters (about {cm_to_inch(height)} inches) tall.")
print(f"He's {weight} kilograms (about {kg_to_pound(weight)} pounds) heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")