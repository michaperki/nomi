# This is the main file for the financial dashboard project

# Importing the necessary libraries
from data_transform import data_transform
from data_import import data_import
from data_export import data_export
from is_running_in_domo import is_running_in_domo

# Defining the main function
def main():
    # check if the code is running in domo
    if is_running_in_domo():
        print("this code is running in domo")

    # import the data
    data_import()

    # transform the data
    data_transform()

    # export the data
    data_export()

if __name__ == "__main__":
    main()