filename = 'programming.txt'

# the second option can be: 
# r  - read
# r+ - read/write
# a  - append
# w  - write ()
#
# Be careful opening a file in write mode ('w') 
# because if the file does exist, Python will erase 
# the contents of the file before returning the file object.
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games!\n")