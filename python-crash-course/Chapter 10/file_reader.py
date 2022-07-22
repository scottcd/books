# Read a file and print the contents
with open('pi_digits.txt') as file_object:
    # contents = file_object.read()
    # print(contents)
    for line in file_object:
        print(line)