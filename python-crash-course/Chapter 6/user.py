user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

# loop through and get all information in a dictionary
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# loop through all keys; this is defau;t behavior
# if you were to just loop the dictionary
# i.e. 'for key in user_0'
for key in user_0.keys():
    print(f"\nKey: {key}")

# loop through all values
for value in user_0.values():
    print(f"\Value: {value}")

# Use a set to only get unique items
for value in set(user_0.values()):
    print(f"\Value: {value}")