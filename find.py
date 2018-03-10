from os import walk, path

f = input("Find: ")                 # Ask for file to find; EXACT
for root, dirs, files in walk("/"):     # Go through everything
  if f in files:                        # If filename found
    print(path.join(root,f))            # Print it out, adding directory to filename