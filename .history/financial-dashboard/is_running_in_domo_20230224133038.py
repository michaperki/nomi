# Description: This is a sample python file

# Importing the necessary libraries
import os

# Defining the detect_environment function
def is_running_in_domo():
    DOMO_ENV = r"/home/domo"
    return os.path.exists(DOMO_ENV)

if __name__ == "__main__":
    detect_environment()