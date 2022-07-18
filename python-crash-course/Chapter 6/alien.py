alien_0 = {'color': 'green', 'points': 5}

alien_0['x_position'] = 0
alien_0['yposition'] = 10
print(alien_0)

# delete a key-value pair
del alien_0['points']
print(alien_0)

#print(f"Alien 0 is {alien_0['color']}.")
print(f"The alien is now {alien_0['color']}.")

alien_0['color'] = 'red'
print(f"The alien is now {alien_0['color']}.")
