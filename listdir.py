# Very basic recreation of bash's 'ls' command in Python
from os import listdir

directory = input("Directory: ")  # Ask for a directory to list
print(listdir(directory))		      # Print the contents
