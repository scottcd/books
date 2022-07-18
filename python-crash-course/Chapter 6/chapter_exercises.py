# Person
person = {
    'first_name': 'chandler',
    'last_name': 'scott',
    'age': 26,
}

print(person)

# Favorite Number
favorite_numbers = {
    'chandler': 2,
    'lilly': 3,
    'nelson': 28,   # that's how many treats nelson wants
    'uma': 45,      # that's how many treats uma wants
}

# Glossary
programming_glossary = {
    'list slice': 'A portion of a list aquired by index [:]',
    'for': 'Used to loop through a list',
    'in': 'Used to see if something is in a list'
}

# Glossary 2
for term, definition in programming_glossary.items():
    print(f'{term}: {definition}')

# Rivers
rivers = {
    'nile': 'egypt',
    'amazon': 'peru',
    'yellow': 'china',
    'mississipi': 'usa'
}

for river, country in rivers.items():
    print(f'The {river} river runs through {country}.')

for river_name in rivers:
    print(river_name)

for river_country in rivers.values():
    print(river_country)
