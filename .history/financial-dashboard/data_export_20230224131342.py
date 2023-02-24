# Description: This is a sample python file

# Importing the necessary libraries

# Defining the main function
def data_export():
    print("this function exports the data")

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