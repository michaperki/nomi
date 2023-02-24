# Description: This is a sample python file

# Importing the necessary libraries
import os
from is_running_in_domo import is_running_in_domo

# Defining the main function
def data_export():
    # check if the code is running in domo
    if is_running_in_domo():
        print("this code is running in domo")
    else:
        print("this code is not running in domo")
    
    # declare the path "financial-dashboard"
    PATH = "financial-dashboard"

    # for each file in the path
    for file in os.listdir(PATH):
        # if the file is a python file
        if file.endswith(".py"):
            # print the file name
            print(file)

if __name__ == "__main__":
    data_export()