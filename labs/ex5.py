# tells name
my_name = 'Zed A. Shaw'
# tells age
my_age = 35 # not a lie
# tells height in inches
my_height = 74 # inches
# tells weight in punds
my_weight = 180 # lbs
# tells eye color
my_eyes = 'Blue'
# tells teeth color
my_teeth = 'White'
# tells hair color
my_hair = 'Brown'
# converts inches into centimeters
my_heightCM = (my_height * 2.54)
# converts lbs into kilograms
my_weightKG = (my_weight * 0.453592)

print(f"Let's talk about {my_name}.")
print(f"He's {my_heightCM} centimeters tall.")
print(f"He's {my_weightKG} kilograms heavy.")
print("Actually that's not to heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
# adds up all of the code and makes a total
total = my_age + my_height + my_weight
print(f"If i add {my_age} , {my_height} and my {my_weight} I get {total}.")