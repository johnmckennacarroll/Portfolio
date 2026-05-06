#----------------------------
#Step 1: Import libraries
#----------------------------
import pandas as pd



#----------------------------
#step 2: Load data
#----------------------------
df = pd.read_csv("data/call_center_data.csv")

# Cleaning column names, replacing spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("\nUpdated column names:")
print(df.columns)



#----------------------------
# Step 3: Convert percentages to numbers
#----------------------------
# Raw data had Answer Rate and service level as strings
df["answer_rate"] = df["answer_rate"].str.replace("%", "").astype(float)
df["service_level_(20_seconds)"] = df["service_level_(20_seconds)"].str.replace("%", "").astype(float)



#----------------------------
#Step 4: Converting time columns to seconds
#----------------------------
# converting HH:MM:SS to total seconds
def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(":"))
    return h * 3600 + m * 60 + s


df["answer_speed_(avg)"] = df["answer_speed_(avg)"].apply(time_to_seconds)
df["talk_duration_(avg)"] = df["talk_duration_(avg)"].apply(time_to_seconds)
df["waiting_time_(avg)"] = df["waiting_time_(avg)"].apply(time_to_seconds)



#----------------------------
#Step 5: Checking results
#----------------------------
print("\nUpdated Data Types:")
print(df.dtypes)

print("\nPreview cleaned data:")
print(df.head())



#----------------------------
#Step 6: Save cleaned data
#----------------------------
df.to_csv("outputs/clean_call_center_data.csv", index=False)

print("\nCleaned dataset saved!")