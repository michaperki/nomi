# This is the main file for the financial dashboard project

# Importing the necessary libraries
import os
from func import func

# Defining the main function
def main():
    print("hello world")
    func()

    # declare the path "financial-dashboard"
    PATH = "financial-dashboard"

    # for each file in the path
    for file in os.listdir(PATH):
        # if the file is a python file
        if file.endswith(".py"):
            # print the file name
            print(file)




if __name__ == "__main__":
    main()