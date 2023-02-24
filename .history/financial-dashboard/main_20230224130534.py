# This is the main file for the financial dashboard project

# Importing the necessary libraries
from func import func

# Defining the main function
def main():
    print("hello world")
    func()

    # get the text that is in the file func.py and print it
    with open("financial-dashboard/func.py", "r") as f:
        print(f.read())

if __name__ == "__main__":
    main()