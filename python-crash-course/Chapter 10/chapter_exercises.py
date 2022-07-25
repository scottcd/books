# Learning Python
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

# Learning C
for line in lines:
    print(line.replace('Python', 'C').strip())

# Guest
name = input('Please enter your name: ')

with open('user_name.txt', 'w') as file_object:
    file_object.write(name)

# Guest Book
name = ''
while name != 'q':
    with open('user_name.txt', 'a') as file_object:
        name = input('Please enter your name: ')
        file_object.write(f'{name}\n')

