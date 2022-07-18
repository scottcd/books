# Conditional Tests
age = 10
print("Is age > 11? I predict True.")
print(age > 11)

# More Conditional Tests
name1 = 'chandler'
name2 = 'Chandler'

print(name1 == name2)
print(name1 == name2.lower())
print(name1 == name2 and age < 8)
print(name1 == name2 or age == 8)

# Alien Colors #1
alien_color = 'yellow'

if alien_color == 'green':
    print("You just got 5 points!")

# Alien Colors #2
alien_color = 'yellow'

if alien_color == 'green':
    print("You just got 5 points!")
else:
    print("You just got 10 points!")

# Alien Colors #3
alien_color = 'yellow'

if alien_color == 'green':
    print("You just got 5 points!")
elif alien_color == 'yellow':
    print("You just got 10 points!")
elif alien_color == 'red':
    print("You just got 15 points!")

# Stages of Life
age = 54

if age < 2:
    print('You are a baby.')
elif age >= 2 and age < 4:
    print('You are a toddler.')
elif age >= 4 and age < 13:
    print('You are a kid.')
elif age >= 13 and age < 20:
    print('You are a teen.')
elif age >= 20 and age < 65:
    print('You are an adult.')
elif age > 65:
    print('You are an elder.')

# Favorite Fruit
favorite_fruits = ['apples', 'grapes', 'bananas']

if 'apples' in favorite_fruits:
    print('We love apples!')
if 'kiwis' in favorite_fruits:
    print('We love kiwis!')
if 'grapes' in favorite_fruits:
    print('We love grapes!')
if 'strawberries' in favorite_fruits:
    print('We love strawberries!')
if 'bananas' in favorite_fruits:
    print('We love bananas!')

# Hello Admin
usernames = ['admin', 'chandler', 'joe', 'machine']

for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f'Hello {user}, welcome to the system!')

# No Users
usernames = []

if not usernames:
    print('Need some users')

# Ordinal Numbers
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(f'{number}st')
    if number == 2:
        print(f'{number}nd')
    if number == 3:
        print(f'{number}rd')
    if number > 3:
        print(f'{number}th')