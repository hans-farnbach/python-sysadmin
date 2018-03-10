from os import execlp                   # Calling child process

process = input("Process: ")        # Ask for a process
execlp(process, "python")       # Run it, putting something as a 2nd arg so the OS knows python invoked this process