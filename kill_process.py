# Given a process name, kills or suspends the process
import psutil                           # pip install psutil

proc = input("Process: ")               # Ask for the name of a process to kill
ks = input("Kill (y/n)?")               # Ask to kill, otherwise will suspend

if ks[0] == "y" or ks[0] == "Y":        # If we should kill; looks at only first character so that user can type "y" or "yes"
  for p in psutil.process_iter():       # Go through process list
    if p.name() == proc:                # Find it
      p.kill()                          # Kill it

else:                                   # No kill
  for p in psutil.process_iter():       # Go through
    if p.name() == proc:                # Find it
      p.suspend()                       # Go sleep
