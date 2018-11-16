# import an argument variable
from sys import argv
# unpack argv, get assigned to two variable
script, filename = argv
# use a new command 'open' to open a file
txt = open(filename)
# print a format string
print(f"Here's your file {filename}:")
# we learn a new function called 'read', to read the file
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

# If you want to print a file, you need to open the file first, 
# then use the function .read()