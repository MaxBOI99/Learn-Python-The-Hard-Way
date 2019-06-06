# creates mapping of states to abbreviation
states = {
    'Massachusetts': 'MA',
    'Connecticut': 'CT',
    'California': 'CA',
    'Maine': 'ME',
    'Rhode Island': 'RI',
}

# creates a basic set of states of some cities in them
cities = {
    'MA' : 'Worcester',
    'RI' : 'Providence',
    'CA' : 'San Diego',
}

# add some more cities
cities['ME'] = 'Portland'
cities['CT'] = 'Bridgeport'

# print out some cities 
print('-' * 10)
print("ME has: ", cities['ME'])
print("MA has: ", cities['MA'])

# prints some states
print('-' * 10)
print("Rhode Island's abbreviation is: ", states['Rhode Island'])
print("Connecticut's abbreviation is: ", states['Connecticut'])

# do it by using the state then cities dict
print('-' * 10)
print("Rhode Island has: ", cities[states['Rhode Island']])
print("Connecticut has: ", cities[states['Connecticut']])

# print every state abbreviation
print("-" * 10)
for state, abbrev in list(states.items()):
   print(f"{state} is abbreviated {abbrev}")
    
# prints every city in state
print("-" * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
    
# now do both at the same time
print('-' * 10)
for state, abbrev in list (states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has a city {cities[abbrev]}")
    
    print('-' * 10)
    # safely get an abbreviation bt state that might not be there 
    state = states.get('Ohio')
    
    if not state:
        print("Sorry, no Ohio")
        
# get a city with a default value
city = cities.get('OH', 'Columbus')
print(f"The city for the state 'OH' is: {city}")