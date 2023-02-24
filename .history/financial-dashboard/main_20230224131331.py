# This is the main file for the financial dashboard project

# Importing the necessary libraries
import os
from data_transform import data_transform
from data_import import data_import
from data_export import data_export

# Defining the main function
def main():
    # import the data
    data_import()

    # transform the data
    data_transform()

    # export the data
    data_export()

if __name__ == "__main__":
    main()