# Message
def display_message():
    '''Display what we are learning'''
    print("We are learning how to use functions!")

display_message()

# Favorite Book
def favorite_book(title):
    """Prints our favorite book"""
    print(f'One of my favorite books is {title.title()}.')

favorite_book('Frankenstein')

# T-Shirt
def make_shirt(shirt_size, shirt_color = 'green'):
    """Print a summary of shirt color and size"""
    print(f"A {shirt_size}, {shirt_color} shirt.")

make_shirt('large', 'red')
make_shirt('large')
make_shirt(shirt_color='grey', shirt_size='small')