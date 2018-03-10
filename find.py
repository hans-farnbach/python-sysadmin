# Asks for a filename and tells you where it is

from os import walk, path

f = input("Find: ")                     # Ask for file to find; EXACT
for root, dirs, files in walk("/"):     # Go through everything
  if f in files:                        # If filename found....
    print(path.join(root,f))            #   print it out, adding directory to filename
