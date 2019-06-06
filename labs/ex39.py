# creates mapping of states to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'Claifornia': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

# creates a basic set of states of some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville',
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities 
print('-' * 10)
print("NY has: ", cities['NY'])
print("OR has: ", cities['OR'])

# prints some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

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
    state = states.get('Texas')
    
    if not state:
        print("Sorry, no Texas")
        
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")