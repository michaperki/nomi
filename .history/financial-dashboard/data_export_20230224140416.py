# Description: This is a sample python file

# Importing the necessary libraries
import os
from is_running_in_domo import is_running_in_domo
from data_export_domo import data_export_domo
from data_export_local import data_export_local

# Defining the main function
def data_export():
    print("this function exports the data")
    data_export_domo if is_running_in_domo() else "1"

if __name__ == "__main__":
    data_export()