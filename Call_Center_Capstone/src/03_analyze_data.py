#-------------------------
# Step 1: Import librtaries
#-------------------------
import pandas as pd



#-------------------------
# Step 2: Load cleaned data
#-------------------------
# using the cleaned data that was saved 
# after running 02_clean_data.py
df = pd.read_csv("outputs/clean_call_center_data.csv")



#-------------------------
# Step 3: View basic statistics
#-------------------------
# averages, minimums, maximums, and spread
print("\nBasic statistics for cleaned data:")
print(df.describe())



#-------------------------
# Step 4: Calculate abandonment rate
#-------------------------
# abandonment rate shows what percent of incoming calls were abandoned
# abandoned calls / incoming calls * 100
df["abandonment_rate"] = (df["abandoned_calls"] / df["incoming_calls"]) * 100



#-------------------------
# Step 5: Check relationships between columns
#-------------------------
# correlation shows how strongly two variables move together
# values close to 1 = strong positive relationship
# values close to -1 = strong negative relationship
# values close to 0 = weak/no relationship
correlation_matrix = df.corr(numeric_only=True)

print("\nCorrelation Matrix:")
print(correlation_matrix)



#-------------------------
#Step 6: Focus on service level relationships
#-------------------------
# sorts correlations with service level from strongest to weakest
service_level_corr = correlation_matrix["service_level_(20_seconds)"].sort_values(ascending=False)

print("\nCorrelation with Service Level:")
print(service_level_corr)



#-------------------------
# Step 7: Save updated dataset
#-------------------------
df.to_csv("outputs/analyzed_call_center_data.csv", index=False)

print("\nAnalyzed dataset saved!")