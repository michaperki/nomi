# Description: This is a sample python file

# Importing the necessary libraries
import pandas as pd

# Defining the data_import function
def data_import():
    print("this function imports the data")
    PATH = "../sample_data.xlsx"
    df = pd.read_excel(PATH)
    print(df)



if __name__ == "__main__":
    data_import()