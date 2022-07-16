# Pizzas
pizza_toppings = ['pepperoni', 'cheese', 'pineapple']

for pizza_topping in pizza_toppings:
    print(f'I like {pizza_topping} on pizza. ')

print(f'\nI really like pizza; especially, the ones that taste good.\n' +
'I like to eat pizza with my friends.\n' +
'That is the best part of pizza')

# Animals
farm_animals = ['pig', 'chicken', 'cow']

for farm_animal in farm_animals:
    print(f'A {farm_animal} would be good on a farm.')

print("These would all be good on a farm.")

# Couting to Twenty 
for value in range(1,21):
    print(value)

# One Million
# for value in range(1, 1_000_001):
    # print(value)

# Summing a Million
numbers = list(range(1,1_000_001))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# Odd Numbers  
odd_numbers = list(range(1,21,2))
for number in odd_numbers:
    print(number)

# Threes 
numbers = list(range(1,21,3))
for number in numbers:
    print(number)

# Cubes
numbers = list(range(1,11))

for number in numbers:
    print(number ** 3)

# Cube Comprehension
numbers = [number**3 for number in range(1,11)]
print(numbers)

# Slices
print(f'The first three items in the list are: {numbers[:3]}')
print(f'The middle three items in the list are: {numbers[4:-3]}')
print(f'The last three items in the list are: {numbers[3:]}')

# More Loops
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friends_foods:
    print(food)
    
# Buffet
foods = ('carrot', 'steak', 'bread', 'corn', 'rice')
for food in foods:
    print(food)

foods = ('carrot', 'chicken', 'bread', 'beans', 'rice')
for food in foods:
    print(food)