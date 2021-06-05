#Make sure you set your directory to the path where all files are stored

import os
try:
    path = "C:\Users\glee3\Downloads"
    os.chdir(path)
    #Check if Python version is above 3.6 to user f-string
    print(f"Your current directory is successfully set to {path}")
except OSError:
    print("OS raised an error: check if the path exists or the name is the same")
