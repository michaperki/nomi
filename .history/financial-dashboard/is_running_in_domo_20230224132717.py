# Description: This is a sample python file

# Importing the necessary libraries
import os

# Defining the detect_environment function
def detect_environment():
    DOMO_ENV = r"/home/domo"
    if os.path.exists(DOMO_ENV):
        print("domo environment detected")
    else:
        print("domo environment not detected")

if __name__ == "__main__":
    detect_environment()