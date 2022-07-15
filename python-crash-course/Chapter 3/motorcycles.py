from time import monotonic


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# edit the first list entry
motorcycles[0] = 'ducati'
print(motorcycles)

# add to the list
motorcycles.append('honda')
print(motorcycles)

# insert to the front of the list
motorcycles.instert(0, 'zz')

# remove by index
del motorcycles[0]

# remove by value
motorcycles.remove('yamaha')

