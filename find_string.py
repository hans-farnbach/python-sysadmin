# Given a filename and a string, find the location of the file
# and where in the file the string is located
from os import walk, path

f = input("File: ")                     # Ask for file to find; EXACT
s = input("String: ")                   # Ask for string to find in file; EXACT

for root, dirs, files in walk("/"):     # Go through everything
  if f in files:                        # If filename found....
    filepath = path.join(root,f)        #   store the full path
    
    # Search the filename for that string
    with open(filepath) as f:
      data = [line.strip() for line in f.readlines()]
      for linenum, line in enumerate(data):
        character = line.find(s)
        
        # Found the string; Print everything out
        if character != -1:
          to_print = "String '" + s + "' found on line " + str(linenum)
          to_print += ", starting at character " + str(character)
          print(to_print)
          quit()
# Didn't find the string
print("String not found")
