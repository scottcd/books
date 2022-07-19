# Rental Car
rental_car = input("What kind of rental car would you like? ")
print(f"I will try to get you a {rental_car} rental car!")

# Restaurant Seating
party_size = input("How many people are in your dinner group? ")
party_size = int(party_size)

if party_size  >= 8:
    print("You will need to wait for a table..")
else:
    print("Right this way to be seated!")

# Multiples of Ten
number = input("Enter a multiple of ten: ")
number = int(number)

if (number % 10) == 0:
    print("Nice, a multiple of ten!")
else:
    print("That is not a multiple of ten.")

# Deli
sandwich_orders = ['pastrami', 'ham & cheese', 'peanut butter']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    if order == 'pastrami':
        print('Sorry we are out of pastrami!')
        continue

    finished_sandwiches.append(order)
    print(f"I finished your {order} sandwich!")

