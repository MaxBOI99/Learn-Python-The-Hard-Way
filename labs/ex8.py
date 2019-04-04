formatter= "{} {} {} {}" # makes a placeholder variable

print(formatter.format(1,2,3,4)) # formats and prints
print(formatter.format("one", "two", "three", "four")) # formats and prints
print(formatter.format(formatter , formatter , formatter , formatter)) # formats and prints
print(formatter.format(
    "Apex is doodoo",
    "Apex is doodoo",
    "Apex is doodoo",
    "Apex is doodoo" # formats and prints specified text
))