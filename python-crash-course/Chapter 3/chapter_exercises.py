# Names
from audioop import reverse


names = ['Harry', 'Mairon', 'Lilly']

print(names[0])
print(names[1])
print(names[2])

# Greetings
message = f"Thanks {names[0]}, you're the best!"
print(message)

message = f"Thanks {names[1]}, you're the best!"
print(message)

message = f"Thanks {names[2]}, you're the best!"
print(message)

# Your Own List
cool_vehicles = ['plane', 'tank', 'yatch']

statement = f"I would love to own a {cool_vehicles[0]}"
print(statement)
statement = f"I would love to own a {cool_vehicles[1]}"
print(statement)
statement = f"I would love to own a {cool_vehicles[2]}"
print(statement)

# Guest List
guest_list = ['chandler', 'lilly', 'nelson', 'uma']
invitation = f"Hey {guest_list[0]}, you're invited to a party!"
print(invitation)
invitation = f"Hey {guest_list[1]}, you're invited to a party!"
print(invitation)
invitation = f"Hey {guest_list[2]}, you're invited to a party!"
print(invitation)
invitation = f"Hey {guest_list[3]}, you're invited to a party!"
print(invitation)

# Changing Guest List
print(f"guest_list[2] can't make it!")
del guest_list[2]

print(guest_list)

# More Guests
print('Guess what? I found a bigger table! We can have more friends.')

guest_list.insert(0, 'Barack Obama')
guest_list.insert(3, 'Mike Tyson')
guest_list.append('Steve')

invitation = f"Hey {guest_list[0]}, you're invited to a party!"
print(invitation)
invitation = f"Hey {guest_list[1]}, you're invited to a party!"
print(invitation)
invitation = f"Hey {guest_list[2]}, you're invited to a party!"
print(invitation)
invitation = f"Hey {guest_list[3]}, you're invited to a party!"
print(invitation)
invitation = f"Hey {guest_list[4]}, you're invited to a party!"
print(invitation)
invitation = f"Hey {guest_list[5]}, you're invited to a party!"
print(invitation)

# Shrinking Guest List
print('Sorry my mom said only 2 people..')
person = guest_list.pop(0)
print(f'{person} cannot come!')
person = guest_list.pop(0)
print(f'{person} cannot come!')
person = guest_list.pop(0)
print(f'{person} cannot come!')
person = guest_list.pop(0)
print(f'{person} cannot come!')


invitation = f"Hey {guest_list[0]}, you're invited to a party!"
print(invitation)
invitation = f"Hey {guest_list[1]}, you're invited to a party!"
print(invitation)

del guest_list[0]
del guest_list[0]

print(guest_list)

# Seeing the World
places_tovisit = ['Greece', 'Canada', 'Panama']

print(places_tovisit)
print(sorted(places_tovisit))
print(places_tovisit)

print(sorted(places_tovisit, reverse=True))
print(places_tovisit)

places_tovisit.reverse()
print(places_tovisit)
places_tovisit.reverse()
print(places_tovisit)

places_tovisit.sort()
print(places_tovisit)
places_tovisit.sort(reverse=True)
print(places_tovisit)

# Dinner Guests
print(len(guest_list))

# Every Function
cool_names = ['eric', 'ornell', 'anton', 'perry']
print(cool_names)
print(sorted(cool_names))
print(cool_names)
print(sorted(cool_names, reverse=True))
print(cool_names)
cool_names.sort()
print(cool_names)
cool_names.sort(reverse=True)
print(cool_names)
cool_names.reverse()
print(cool_names)

# Intentional Error
list = []
# item = list[-1] THIS THROWS ERROR
list.append('one')
print(list[-1])