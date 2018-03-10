# Given the name of a process, will execute process
from os import execlp           # Calling child process

process = input("Process: ")    # Ask for a process name to run
execlp(process, "python")       # Run it, putting something as a 2nd arg so the OS knows Python invoked this process
