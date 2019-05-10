people = 30  # sets mun of people to 30
cars = 40  # sets num of cars to 40 
trucks = 15  # sets num of trucks to 15


if cars > people: # sets vaiables to more or less than other variables
    print("We should take the cars.")  
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
 
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")