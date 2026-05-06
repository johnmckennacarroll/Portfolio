
# Step 1: Import libraries
# --------------------------
# pandas is used for working with data tables
import pandas as pd



# Step 2: Load the dataset
# --------------------------
# Read CSV file from the data folder
df = pd.read_csv("data/call_center_data.csv")


# Step 3: Preview Dataset
#--------------------------
# Printing to show first 5 rows of data 
print("First 5 rows of the dataset:")
print(df.head())



# Step 4: Check dataset size
#-------------------------
# Check amount of rows and columns in dataset
print("\nDataset shape (rows, columns):")
print(df.shape)



# Step 5: View column names
#-------------------------
# Print column names
print("\nColumn names:")
print(df.columns)



# Step 6: Check data types
#--------------------------
# Checking data type of each column
print("\nData types:")
print(df.dtypes)



# Step 7: Check for missing values in dataset
#-----------------------------
# Shows missing or blank values in each column
print("\nMissing values per column:")
print(df.isnull().sum())



# Step 8: Basic statistics
#-------------------------
# Summary stats for numeric columns
print("\nBasic statistics:")
print(df.describe())



