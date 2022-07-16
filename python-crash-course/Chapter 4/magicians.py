magicians = ['alice', 'david', 'caroline']

# print out each name in magician
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f'I cannot wait to see your next trick, {magician.title()}.\n')

# since this is indented left of the loop, it will not run in our for loop
print("Thank you everyone. That was a great show!")
