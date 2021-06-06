#Make sure you set your directory to the path where all files are stored
import os.path
from os import path

#path.exists() returns Boolean
#Python doesn't accept Boolean + String combination fyi

def check():
    #Do you know the cost of IF vs TRY/EXCEPT?
    try:
        path.exists(pathname)
        print(f"{pathname} : this path is valid - you can use them to")
    except OSError:
        #Python version needs to be higher than 3.6 to use f-string
        print(f"OS raised an error: check if the path {pathname} exists or the name is the same")

import pandas as pd

def import_csv(filename):
    df = pd.read_csv(f"{pathname}/{filename}")
    return df

if __name__ == "__main__":
    pathname = "C:/Users/glee3/Downloads"
    check()
    first_df =import_csv('transfers (2).csv')
    print(first_df)




