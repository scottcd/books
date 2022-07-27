# 4.1
secret = 4
guess = 2

if secret > guess:
    print('too low!')
elif secret < guess:
    print('too high!')
else:
    print("You guessed the correct number!")

# 4.2
small = True
green = 0.0

if small:
    if green:
        print('small and green')
    else:
        print('small and not green')
else:
    if green:
        print('big and green')
    else:
        print('big and not green')
